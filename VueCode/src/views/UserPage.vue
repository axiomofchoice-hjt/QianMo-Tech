<template>
  <el-scrollbar style="height: 100%">
    <el-row type="flex" justify="center">
      <el-col :xs="24" :sm="22" :md="21" :lg="20" :xl="16">
        <el-container>
          <el-header>
            <x-header />
          </el-header>
          <el-main>
            <router-view></router-view>
          </el-main>
          <el-footer> </el-footer>
        </el-container>
      </el-col>
    </el-row>
  </el-scrollbar>
</template>
<script>
import xHeader from "@/components/UserHeader.vue";
export default {
  data() {
    return {};
  },
  components: {
    xHeader,
  },
};
</script>