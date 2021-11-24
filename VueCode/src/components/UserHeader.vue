<template>
  <div>
    <div class="left-col" :style="{ width: QianMoWidth, background: bgcolor }">
      <strong>阡陌科技</strong>
    </div>
    <el-menu
      :default-active="active()"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      :background-color="bgcolor"
      text-color="#fff"
      active-text-color="#ffd04b"
      :router="true"
      :style="{ marginLeft: QianMoWidth }"
    >
      <el-menu-item index="/user/info"
        ><i class="el-icon-s-custom"></i>个人信息</el-menu-item
      >
      <el-menu-item index="/user/message"
        ><i class="el-icon-message"></i>消息通知</el-menu-item
      >
      <el-menu-item index="/user/vehicle"
        ><i class="el-icon-bicycle"></i>车辆管理</el-menu-item
      >
      <el-menu-item index="/user/record"
        ><i class="el-icon-edit-outline"></i>违法记录</el-menu-item
      >
      <el-menu-item index="/" style="position: absolute; right: 0"
        ><i class="el-icon-back"></i>退出</el-menu-item
      >
    </el-menu>
  </div>
</template>
<script>
export default {
  data() {
    return {
      QianMoWidth: "160px",
      bgcolor: "#545c64",
    };
  },
  methods: {
    active() {
      if (this.$route.path.indexOf("/user/info") == 0) return "/user/info";
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
  position: absolute;
  z-index: 1;
}
</style>