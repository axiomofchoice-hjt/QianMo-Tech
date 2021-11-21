<template>
  <div class="xdisplay" style="padding-left: 100px; padding-right: 100px;">
    <h2 style="text-align: center">修改违法事件</h2>
    <el-form ref="form" :model="formInfo" label-width="100px">
      <el-form-item label="时间：">
        <el-date-picker
          v-model="formInfo.date"
          x-align="right"
          type="date"
          placeholder="选择日期"
          :picker-options="DateOptions"
        >
        </el-date-picker>
        &nbsp;
        <el-time-picker
          v-model="formInfo.time"
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
        <el-checkbox v-model="formInfo.illegal1">闯红灯</el-checkbox>
        <el-checkbox v-model="formInfo.illegal2">逆行</el-checkbox>
        <el-checkbox v-model="formInfo.illegal3">未戴头盔</el-checkbox>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit" style="margin: 0 15px;">提交</el-button>
        <router-link to="/admin/record"><el-button>取消</el-button></router-link>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import tools from '@/tools'
import dayjs from 'dayjs'
export default {
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
        illegal1: false,
        illegal2: false,
        illegal3: false,
      },
      cameraList: [],
      partitionList: [],
      addressDisabled: true,
      addressPlaceholder: "请先选择分区",
      addressList: [],
    };
  },
  methods: {
    onSubmit() {
      var camera = null;
      console.log(this.cameraList);
      for (let i of this.cameraList)
      if (i.address === this.formInfo.address)
        camera = i;
      var illegal = [];
      if (this.formInfo.illegal1) illegal.push("1");
      if (this.formInfo.illegal2) illegal.push("2");
      if (this.formInfo.illegal3) illegal.push("3");
      var record = {
        time: this.formInfo.date + ' ' + this.$dayjs(this.formInfo.time).format("HH:mm:ss"),
        partition: camera.partition,
        street: camera.street,
        address: camera.address,
        identity: this.formInfo.identity,
        illegal_nature: illegal.join(","),
        carPlate: this.formInfo.carplate,
        point: camera.point,
      }
      console.log(record);
      this.$http.post("/worker/add", record).then(() => {
        console.log("add record ok");
      });
      this.$router.push("/admin/record");
    },
    partitionChange() {
      this.addressDisabled = false;
      this.addressPlaceholder = "请选择";
      this.addressList = [];
      this.formInfo.address = "";
      for (let i of this.cameraList)
      if (i.partition === this.formInfo.partition)
        this.addressList.push(i.address);
    },
  },
  created() {
    tools.getCameraList(this.$http, (list) => {
      this.cameraList = list;
      console.log(list);
      this.partitionList = tools.collectAttr(list, "partition")
      // this.addressList = tools.collectAttr(list, "");
    })
    
      var query = {
        pagesize: 5,
        pageIndex: 1,
        timeOrder: "ASC",
        serial: this.$route.params.serial,
      }
      this.$http.post("worker/show_illegal", query).then((response) => {
        console.log(response);
        let content = response.data.data.content;
        let labels = response.data.data.labels;
        var rec = tools.trans(labels, content, tools.illegalNameMap)[0];
        var dj = dayjs(rec.time);
        this.formInfo = {
          date: dj.format("YYYY-MM-DD"),
          time: dj.toDate(),
          partition: rec.partition,
          identity: rec.identity,
          carplate: rec.carplate,
        }
        this.partitionChange();
        this.formInfo.address = rec.address;

        
        rec.illegalList = [];
        for (let j of rec.illegalnature.split(",")) {
          if (j == '1') this.formInfo.illegal1 = true;
          if (j == '2') this.formInfo.illegal2 = true;
          if (j == '3') this.formInfo.illegal3 = true;
        }

        console.log(this.formInfo);
      })
  },
};
</script>