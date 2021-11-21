<template>
  <div class="xdisplay" style="padding-left: 100px; padding-right: 100px">
    <h2 style="text-align: center">{{ title }}</h2>
    <el-form ref="form" label-width="100px">
      <el-form-item label="时间：">
        <el-date-picker
          v-model="formInfo.date"
          x-align="right"
          type="date"
          placeholder="选择日期"
          :clearable="false"
          :picker-options="DateOptions"
        >
        </el-date-picker>
        &nbsp;
        <el-time-picker
          v-model="formInfo.time"
          :clearable="false"
          placeholder="选择时间"
        >
        </el-time-picker>
      </el-form-item>
      <el-form-item label="分区：">
        <el-select
          v-model="formInfo.partition"
          filterable
          placeholder="请选择"
          @change="partitionChange"
          style="width: 300px"
        >
          <el-option
            v-for="item in partitionList"
            :key="item"
            :label="item"
            :value="item"
          >
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="地点：" ref="address">
        <el-select
          v-model="formInfo.address"
          filterable
          :placeholder="addressPlaceholder"
          :disabled="addressDisabled"
          style="width: 300px"
        >
          <el-option
            v-for="item in addressList"
            :key="item"
            :label="item"
            :value="item"
          >
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="身份信息：">
        <el-input
          v-model="formInfo.identity"
          placeholder="请输入身份信息"
        ></el-input>
      </el-form-item>
      <el-form-item label="车牌信息：">
        <el-input
          v-model="formInfo.carplate"
          placeholder="请输入车牌信息"
        ></el-input>
      </el-form-item>
      <el-form-item label="违法类型：">
        <el-checkbox-group v-model="formInfo.illegal">
          <el-checkbox label="闯红灯"></el-checkbox>
          <el-checkbox label="逆行"></el-checkbox>
          <el-checkbox label="未戴头盔"></el-checkbox>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="上传图片：">
        <x-upload ref="xUpload"> </x-upload>
      </el-form-item>
      <el-form-item>
        <el-button
          type="primary"
          @click="onSubmit"
          :disabled="!submitable"
          style="margin: 0 15px"
          >提交</el-button
        >
        <el-button @click="$router.push('/admin/record')">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import tools from "@/tools";
import dayjs from "dayjs";
import xUpload from "@/components/AdminNewRecordUpload";
export default {
  components: {
    xUpload,
  },
  data() {
    return {
      DateOptions: {
        disabledDate(time) {
          return time.getTime() > Date.now();
        },
      },
      formInfo: {
        date: dayjs().format("YYYY-MM-DD"),
        time: Date.now(),
        partition: "",
        address: "",
        identity: "",
        carplate: "",
        illegal: [],
      },
      cameraList: [],
      partitionList: [],
      addressDisabled: true,
      addressPlaceholder: "请先选择分区",
      addressList: [],
    };
  },
  computed: {
    title() {
      return typeof this.$route.params.serial === "string"
        ? "修改违法事件"
        : "添加违法事件";
    },
    submitable() {
      console.log(this.formInfo.illegal);
      return (
        this.formInfo.address !== "" &&
        this.formInfo.identity !== "" &&
        this.formInfo.carplate !== "" &&
        this.formInfo.illegal.length > 0 &&
        this.$refs.xUpload.fileList.length !== 0
      );
    },
  },
  methods: {
    // 得到表单里 time 字符串
    getFormTimeStr() {
      var dj = this.$dayjs(this.formInfo.time);
      var date = this.$dayjs(this.formInfo.date);
      // console.log(dj, date);
      // dj.year(date.year());
      // dj.month(date.month());
      // dj.day(date.day());
      return this.$dayjs(date.format("YYYY-MM-DD") + " " + dj.format("HH:mm:ss")).utc().format("YYYY-MM-DD HH:mm:ss");
    },
    // 得到表单里违法性质字符串
    getFormIllegalStr() {
      var illegalList = [];
      for (let i of this.formInfo.illegal)
        illegalList.push("" + tools.illegalName.indexOf(i));
      return illegalList.join(",");
    },
    // 提交按钮的事件
    onSubmit() {
      var camera = null;
      console.log(this.cameraList);
      for (let i of this.cameraList)
        if (i.address === this.formInfo.address) camera = i;

      // Promise.all 来多图片上传
      var promiseList = [];
      for (let pic of this.$refs.xUpload.fileList) {
        if (pic.backUrl === undefined) {
          var formData = new FormData();
          formData.append("photo", pic.raw);
          promiseList.push(this.$http.post("/picture/getImg", formData));
        }
      }
      Promise.all(promiseList).then((responseList) => {
        console.log(responseList);
        let pictures = [];
        for (let pic of this.$refs.xUpload.fileList)
          if (pic.backUrl !== undefined) pictures.push(pic.backUrl);
        for (let res of responseList) {
          pictures.push("/static/photo/" + res.data.filename);
        }
        console.log(pictures);
        var record = {
          time: this.getFormTimeStr(),
          partition: camera.partition,
          street: camera.street,
          address: camera.address,
          record: pictures.join(" "),
          identity: this.formInfo.identity,
          illegal_nature: this.getFormIllegalStr(),
          carPlate: this.formInfo.carplate,
          point: camera.point,
        };
        // 提交 record
        if (typeof this.$route.params.serial == "string") {
          Object.defineProperty(record, "serial", {
            value: this.$route.params.serial,
            enumerable: true,
          });
          console.log("ChangeRecord:", record);
          this.$http.post("/worker/edit", record).then(() => {
            console.log("change record ok");
          });
        } else {
          console.log("NewRecord:", record);
          this.$http.post("/worker/add", record).then(() => {
            console.log("add record ok");
          });
        }
        this.$router.push("/admin/record");
      });
    },
    // 分区改变的事件
    partitionChange() {
      this.addressDisabled = false;
      this.addressPlaceholder = "请选择";
      this.addressList = [];
      this.formInfo.address = "";
      // 筛选该分区的所有地点至 this.addressList
      for (let i of this.cameraList)
        if (i.partition === this.formInfo.partition)
          this.addressList.push(i.address);
      // 如果该分区只有一个地点，则自动填充
      if (this.addressList.length == 1)
        this.formInfo.address = this.addressList[0];
    },
  },
  created() {
    tools.getCameraList(this.$http, (list) => {
      this.cameraList = list;
      console.log(list);
      this.partitionList = tools.collectAttr(list, "partition");
    });
    // 如果路由带参数，即修改记录
    if (typeof this.$route.params.serial == "string") {
      this.formInfo.date = this.formInfo.time = null;
      var query = {
        pagesize: 5,
        pageIndex: 1,
        timeOrder: "ASC",
        serial: this.$route.params.serial,
      };
      this.$http.post("worker/show_illegal", query).then((response) => {
        console.log(response);
        let content = response.data.data.content;
        let labels = response.data.data.labels;
        var rec = tools.trans(labels, content, tools.illegalNameMap)[0];
        var dj = dayjs(rec.time);
        this.formInfo.date = dj.format("YYYY-MM-DD");
        this.formInfo.time = dj.toDate();
        this.formInfo.partition = rec.partition;
        this.formInfo.identity = rec.identity;
        this.formInfo.carplate=  rec.carplate;
        this.partitionChange();
        this.formInfo.address = rec.address;

        for (let j of rec.illegalnature.split(",")) {
          this.formInfo.illegal.push(tools.illegalName[parseInt(j)]);
        }
        console.log(this.formInfo.illegal);
        this.$refs.xUpload.init(rec.record.split(" "));
        console.log(this.formInfo);
      });
    }
  },
};
</script>