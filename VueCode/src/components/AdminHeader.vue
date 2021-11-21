<template>
  <div>
    <el-row>
      <el-col :span="4" class="left-col" :style="{ background: bgcolor }">
        <strong>阡陌科技</strong>
      </el-col>
      <el-col :span="20">
        <el-menu
          :default-active="active()"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
          :background-color="bgcolor"
          text-color="#fff"
          active-text-color="#ffd04b"
          :router="true"
        >
          <!-- <el-menu-item index="/admin/home"
            ><i class="el-icon-s-home"></i>首页</el-menu-item
          > -->
          <el-menu-item index="/admin/record"
            ><i class="el-icon-edit-outline"></i>违法记录</el-menu-item
          >
          <el-menu-item index="/admin/camera"
            ><i class="el-icon-video-camera"></i>摄像头</el-menu-item
          >
          <el-menu-item index="/admin/screen"
            ><i class="el-icon-s-data"></i>数据可视化</el-menu-item
          >
          <el-menu-item index="/" style="position: absolute; right: 0"
            ><i class="el-icon-back"></i>退出</el-menu-item
          >
        </el-menu>
      </el-col>
    </el-row>
  </div>
</template>
<script>
export default {
  data() {
    return {
      bgcolor: "#545c64",
    };
  },
  methods: {
    active() {
      if (this.$route.path.indexOf("/admin/record") == 0)
        return "/admin/record";
      if (this.$route.path.indexOf("/admin/camera") == 0)
        return "/admin/camera";
      return this.$route.path;
    },
    handleSelect(key, keyPath) {},
  },
};
</script>
<style scoped>
.left-col {
  height: 61px;
  line-height: 60px;
  text-align: center;
  color: white;
  font-size: 25px;
  border-bottom: solid 1px #e6e6e6;
  /* padding-left: 30px; */
}
</style>