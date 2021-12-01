<template>
  <el-scrollbar style="height: 100%">
    <el-row type="flex" justify="center" style="min-width: 960px; max-width: 2080px;">
      <el-col :xs="24" :sm="24" :md="22" :lg="20" :xl="18">
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
import xHeader from "@/components/AdminHeader.vue";
export default {
  data() {
    return {};
  },
  components: {
    xHeader,
  },
};
</script>