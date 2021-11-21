<template>
  <el-scrollbar style="height: 100%">
      <el-row type="flex" justify="center">
        <el-col :xs="24" :sm="22" :md="21" :lg="20" :xl="16">
    <el-container>
      <el-main>
        <x-display />
      </el-main>
    </el-container>
        </el-col>
      </el-row>
  </el-scrollbar>
</template>
<script>
import xDisplay from "../components/Home.vue";
export default {
  components: {
    xDisplay,
  },
};
</script>
<style scoped>
</style>