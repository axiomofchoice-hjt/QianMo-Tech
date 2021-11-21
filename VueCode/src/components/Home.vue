<template>
  <div class="xdisplay">
    <h2 style="text-align: center">阡陌科技 双轮车交通管理系统</h2>
    <el-form :model="form" label-width="100px" style="margin: 0 100px">
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
      <el-form-item>
        <router-link to="/admin/home" style="margin-right: 50px"
          ><el-button type="primary">工作人员登录</el-button></router-link
        >
        <router-link to="/user/info"
          ><el-button type="primary">市民用户登录</el-button></router-link
        >
      </el-form-item>
      <el-form-item>
        <span>还没有账号，<router-link to="/">点此注册账号</router-link></span>
        <span style="margin-left: 100px"
          >忘记密码，<router-link to="/">点此找回密码</router-link></span
        >
      </el-form-item>
    </el-form>
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
