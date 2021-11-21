<template>
  <div class="xdisplay" style="padding-left: 100px; padding-right: 100px;">
    <h2 style="text-align: center">个人信息</h2>
    <el-descriptions border :column="1">
      <el-descriptions-item label="姓名">{{info.name}}</el-descriptions-item>
      <el-descriptions-item label="性别">{{info.sex}}</el-descriptions-item>
      <el-descriptions-item label="手机号">{{info.phone}}</el-descriptions-item>
      <el-descriptions-item label="身份证号">{{info.idnumber}}</el-descriptions-item>
      <el-descriptions-item label="家庭地址">{{info.address}}</el-descriptions-item>
    </el-descriptions>
    <div style="text-align: right; margin-top: 20px;">信息有误？<router-link to="/user/info/change">点我修改</router-link></div>
  </div>
</template>
<script>
export default {
  data() {
    return{
      info:{
        name:"XXX",
        sex:"X",
        phone:"XXXYYYYYYYY",
        idnumber:"AAAAAAYYYYMMDDBBBB",
        address:"浙江省杭州市XXX"
      }
    }
  }
};
</script>
