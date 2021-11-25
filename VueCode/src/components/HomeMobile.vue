<template>
  <div style="padding: 20px;">
    <h2 style="text-align: center">阡陌科技</h2>
    <el-form :model="form" label-width="100px">
      <el-form-item label="用户名：">
        <el-input v-model="form.username" placeholder="请输入用户名"></el-input>
      </el-form-item>
      <el-form-item label="密码：">
        <el-input
          v-model="form.password"
          placeholder="请输入密码"
          show-password
        ></el-input>
      </el-form-item>
    </el-form>
    <router-link to="/admin/home" style="margin-right: 20px"
      ><el-button type="primary">工作人员登录</el-button></router-link
    >
    <router-link to="/user/info" style="float: right;"
      ><el-button type="primary">市民用户登录</el-button></router-link
    >
    <div style="text-align: right; margin-top: 20px;">还没有账号，<router-link to="/">点此注册账号</router-link></div>
    <div style="text-align: right;">忘记密码，<router-link to="/">点此找回密码</router-link></div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },
};
</script>
