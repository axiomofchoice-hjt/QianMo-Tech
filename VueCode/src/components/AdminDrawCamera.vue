<template>
  <div class="xdisplay">
    <h2 style="text-align: center">画停车线</h2>
    <div
      style="margin: 50px auto 20px; text-align: center; position: relative"
      @click="click"
    >
      <!-- <div>
      <el-image :src="frontUrl" fit="none" ref="pic" @load="loaded" ></el-image>
      </div> -->
      <canvas
        ref="canvas"
        :width="w"
        :height="h"
        style="z-index: 100; border-radius: 10px"
        :style="{ background: `url(${frontUrl})` }"
      ></canvas>
    </div>
  </div>
</template>
<script>
import tools from "@/tools";
export default {
  data() {
    return {
      w: 100,
      h: 100,
      frontUrl: "",
    };
  },
  methods: {
    click(event) {
      let canvas = this.$refs.canvas;
      let ctx = canvas.getContext("2d");
      let x = event.clientX - canvas.getBoundingClientRect().left;
      let y = event.clientY - canvas.getBoundingClientRect().top;
      ctx.strokeStyle = "#F00";
      ctx.fillStyle = "#FFF";
      ctx.beginPath();
      ctx.arc(x, y, 10, 0, Math.PI * 2);
      ctx.stroke();
      ctx.fill();
    },
  },
  mounted() {
    this.$http
      .get("static/photo/screenshot.png", { responseType: "blob" })
      .then((response) => {
        var raw = tools.blobToFile(response.data, "233.png");
        this.frontUrl = URL.createObjectURL(raw);
        // 获取宽、高
        var img = new Image();
        img.src = this.frontUrl;
        img.onload = () => {
          this.w = img.width;
          this.h = img.height;
        };
      });
  },
};
</script>
