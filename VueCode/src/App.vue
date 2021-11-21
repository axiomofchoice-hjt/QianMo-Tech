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
};
</script>

<style>
.xdisplay {
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15) !important;
  padding: 20px;
  margin: 1px;
}
</style>