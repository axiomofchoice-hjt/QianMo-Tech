<template>
  <div>
    <el-upload
      class="avatar-uploader"
      ref="otherLicense"
      action
      :file-list="fileList"
      :auto-upload="false"
      :on-preview="handlePicPreview"
      :on-remove="handleRemove"
      :on-change="otherSectionFile"
      list-type="picture-card"
      multiple
    >
      <i class="el-icon-plus avatar-uploader-icon"></i>
    </el-upload>
    <el-dialog :visible.sync="dialogVisible">
      <img width="100%" :src="dialogImageUrl" class="avatar" />
    </el-dialog>
    <!-- <el-button @click="buttonclick"> submit </el-button> -->
  </div>
</template>
<script>
import tools from "@/tools";
export default {
  data() {
    return {
      fileList: [],
      dialogVisible: false,
      dialogImageUrl: "",
      test: "",
    };
  },
  props: ["urls"],
  methods: {
    handlePicPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    handleRemove(file) {
      this.fileList.map((item, index) => {
        if (item.uid == file.uid) {
          this.fileList.splice(index, 1);
        }
      });
    },
    otherSectionFile(file) {
      console.log("onchange");
      this.fileList.push(file);
      console.log(this.fileList);
      const typeArr = ["image/png", "image/gif", "image/jpeg", "image/jpg"];
      const isJPG = typeArr.indexOf(file.raw.type) !== -1;
      // const isLt3M = file.size / 1024 / 1024 < 3;
      if (!isJPG) {
        this.$message.error("只能上传图片");
        this.fileList.pop();
        return;
      }
    },
    buttonclick() {
      for (let pic of this.fileList) {
        var formData = new FormData();
        formData.append("photo", pic.raw);
        this.$http.post("/picture/getImg", formData).then((response) => {
          console.log("upload ok");
          console.log(response);
        });
      }
    },
    init(urls) {
      console.log("urls:", urls);
      for (let url of urls) {
        this.$http
          .get(url, { responseType: "blob" })
          .then((response) => {
            // console.log(response);
            var raw = tools.blobToFile(response.data, "233.png");
            this.fileList.push({
              // name: "noname.jpeg",
              backUrl: url,
              url: URL.createObjectURL(raw)
            });
          });
      }
    },
  },
};
</script>
<style scoped>
.avatar-uploader /deep/ .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  background-color: #fff;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  width: 180px;
  height: 180px;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar-uploader /deep/ .el-upload-list__item {
  overflow: hidden;
  background-color: #fff;
  border: 1px solid #c0ccda;
  border-radius: 6px;
  box-sizing: border-box;
  width: 180px;
  height: 180px;
  margin: 0 8px 8px 0;
  display: inline-block;
}
</style>