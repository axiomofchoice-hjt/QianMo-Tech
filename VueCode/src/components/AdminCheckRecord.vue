<template>
  <div class="xdisplay" style="padding-left: 100px; padding-right: 100px">
    <h2 style="text-align: center">查看违法事件</h2>
    <el-descriptions border :column="1">
      <el-descriptions-item label="事件编号">{{
        info.serial
      }}</el-descriptions-item>
      <el-descriptions-item label="时间">{{
        info.formatTime
      }}</el-descriptions-item>
      <el-descriptions-item label="地点">{{
        info.address
      }}</el-descriptions-item>
      <el-descriptions-item label="身份标志">{{
        info.person
      }}</el-descriptions-item>
      <el-descriptions-item label="违法性质">{{
        info.illegalCode
      }}</el-descriptions-item>
      <el-descriptions-item label="处理状态">{{
        info.stateCode
      }}</el-descriptions-item>
      <el-descriptions-item label="处理者">{{
        info.handler
      }}</el-descriptions-item>
    </el-descriptions>
    <el-image
      v-for="url in frontUrls"
      :key="url"
      style="width: 200px; height: 200px; margin: 5px"
      :src="url"
      fit="fill"
    ></el-image>
    <div style="text-align: right; margin-top: 20px">
      <el-link
        type="primary"
        icon="el-icon-edit"
        :href="'#/admin/record-edit/' + this.$route.params.serial"
        style="font-size: 18px;"
        >信息有误？点我修改</el-link
      >
    </div>
  </div>
</template>
<script>
import tools from "@/tools";
export default {
  data() {
    return {
      info: {},
      frontUrls: [],
    };
  },
  methods: {
    init() {
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
        this.info = tools.trans(labels, content, tools.illegalNameMap)[0];
        tools.illegalElementExtend(this.info);
        for (let backUrl of this.info.pictures) {
          // console.log(backUrl)
          this.$http.get(backUrl, { responseType: "blob" }).then((response) => {
            console.log("get pic:", response);
            var raw = tools.blobToFile(response.data, "233.png");
            this.frontUrls.push(URL.createObjectURL(raw));
          });
        }
      });
    },
  },
  created() {
    this.init();
  },
};
</script>