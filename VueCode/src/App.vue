<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import router from "./router.js";
export default {
  name: "App",
  router,
  created() {
    let isMobile =
      navigator.userAgent.match(
        /(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i
      ) !== null;
    if (isMobile && this.$route.path.substr(0, 7) !== "/mobile") {
      this.$router.push("/mobile" + this.$route.path);
    }
  },
};
</script>

<style>
.xdisplay {
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15) !important;
  padding: 20px;
  margin: 1px;
}
</style>