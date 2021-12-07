<template>
  <div class="xdisplay">
    <h2 style="text-align: center">画停车线</h2>
    <div style="margin: 50px auto 20px; text-align: center; position: relative">
      <canvas
        ref="canvas"
        :width="w"
        :height="h"
        style="z-index: 100; border-radius: 10px"
        :style="{ background: `url(${frontUrl})` }"
        @mousedown="mousedown"
        @mouseup="mouseup"
        @mousemove="mousemove"
        @mouseleave="mouseleave"
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
      pos: [],
      choose: null,
      r: 20,
      lineWidth: 5,
    };
  },
  methods: {
    draw() {
      let canvas = this.$refs.canvas;
      let ctx = canvas.getContext("2d");
      ctx.clearRect(0, 0, this.w, this.h);
      if (this.pos.length == 2) {
        ctx.strokeStyle = "#FFF";
        ctx.lineWidth = this.lineWidth;
        ctx.beginPath();
        ctx.moveTo(this.pos[0][0], this.pos[0][1]);
        ctx.lineTo(this.pos[1][0], this.pos[1][1]);
        ctx.stroke();
      }
      ctx.fillStyle = "#FFF";
      for (let [x, y] of this.pos) {
        ctx.strokeStyle = "#000";
        ctx.lineWidth = this.lineWidth;
        ctx.beginPath();
        ctx.arc(x, y, this.r - this.lineWidth / 2, 0, Math.PI * 2);
        ctx.stroke();

        ctx.strokeStyle = "#FFF";
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.arc(x, y, this.r, 0, Math.PI * 2);
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(x, y, this.r - this.lineWidth, 0, Math.PI * 2);
        ctx.stroke();
      }
    },
    mouseleave(evnet) {
      this.choose = null;
    },
    mousedown(event) {
      let canvas = this.$refs.canvas;
      let x = event.clientX - canvas.getBoundingClientRect().left;
      let y = event.clientY - canvas.getBoundingClientRect().top;

      this.choose = null;
      for (let i = 0; i < this.pos.length; i++) {
        if (
          (this.pos[i][0] - x) * (this.pos[i][0] - x) +
            (this.pos[i][1] - y) * (this.pos[i][1] - y) <=
          this.r * this.r
        ) {
          this.choose = i;
        }
      }
      if (this.choose === null) {
        if (this.pos.length == 0) {
          this.pos.push([x, y]);
          this.pos.push([x, y]);
          this.choose = this.pos.length - 1;
        }
      } else {
        this.pos[this.choose] = [x, y];
      }
      this.draw();
    },
    mousemove(event) {
      let canvas = this.$refs.canvas;
      let x = event.clientX - canvas.getBoundingClientRect().left;
      let y = event.clientY - canvas.getBoundingClientRect().top;
      if (this.choose !== null) {
        this.pos[this.choose] = [x, y];
      }
      this.draw();
    },
    mouseup(event) {
      this.choose = null;
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
