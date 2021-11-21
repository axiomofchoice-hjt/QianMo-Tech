<template>
  <div class="xdisplay" style="padding-left: 100px; padding-right: 100px">
    <h2 style="text-align: center">个人信息</h2>
    <el-form :model="info" label-width="100px">
      <el-form-item label="姓名：">
        <el-input v-model="info.name"></el-input>
      </el-form-item>
      <el-form-item label="性别：">
        <el-input v-model="info.sex"></el-input>
      </el-form-item>
      <el-form-item label="手机号：">
        <el-input v-model="info.phone"></el-input>
      </el-form-item>
      <el-form-item label="身份证号：">
        <el-input v-model="info.idnumber"></el-input>
      </el-form-item>
      <el-form-item label="家庭地址：">
        <el-input v-model="info.address"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit" style="margin: 0 15px"
          >提交</el-button
        >
        <router-link to="/user/info"><el-button>取消</el-button></router-link>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
export default {
  data() {
    return {
      info: {
        name: "XXX",
        sex: "X",
        phone: "XXXYYYYYYYY",
        idnumber: "AAAAAAYYYYMMDDBBBB",
        address: "浙江省杭州市XXX",
      },
    };
  },
  methods: {
    onSubmit() {
      console.log(JSON.stringify(this.info));
      this.$router.push("/user/info");
    },
  },
};
</script>
