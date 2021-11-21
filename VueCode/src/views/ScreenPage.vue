<template>
  <div class="screen-container">
    <header class="screen-header">
      <div>
        <img src="/static/img/head_bg.png" alt="" />
      </div>
      <div class="title-left">
        <span class="datetime">
          <el-button
            type="primary"
            size="mini"
            style="margin-right: 15px"
            @click="$router.go(-1)"
            >返回</el-button
          >
        </span>
      </div>
      <span class="title">双轮车违规驾驶实时监控系统</span>
      <div class="title-right">
        <span class="datetime">当前时间：{{ this.gettime }}</span>
      </div>
    </header>
    <div class="screen-body">
      <section class="screen-left">
        <div
          id="left-top"
          :class="[fullScreenStatus.disposePercent ? 'fullscreen' : '']"
        >
          <!-- 各个市区违规事件处理率图表 -->
          <DisposePercent ref="disposePercent"></DisposePercent>
          <div class="panel-footer"></div>
          <div class="resize">
            <!-- icon-compress-alt -->
            <span
              @click="changeSize('disposePercent')"
              style="color: rgba(70, 212, 255, 0.877)"
              :class="[
                'iconfont',
                fullScreenStatus.disposePercent
                  ? 'icon-compress-alt'
                  : 'icon-expand-alt',
              ]"
            ></span>
          </div>
        </div>
        <div
          id="left-bottom"
          :class="[fullScreenStatus.today ? 'fullscreen' : '']"
        >
          <!-- 今日违规行驶的人次图表 -->
          <Today ref="today"></Today>
          <div class="panel-footer"></div>
          <div class="resize">
            <!-- icon-compress-alt -->
            <span
              @click="changeSize('today')"
              style="color: rgba(70, 212, 255, 0.877)"
              :class="[
                'iconfont',
                fullScreenStatus.today
                  ? 'icon-compress-alt'
                  : 'icon-expand-alt',
              ]"
            ></span>
          </div>
        </div>
      </section>
      <section class="screen-middle">
        <div
          id="middle-top"
          :class="[fullScreenStatus.increased ? 'fullscreen' : '']"
        >
          <!-- 不同市区不同违规事件发生的趋势图表 -->
          <Increased ref="increased"></Increased>
          <div class="panel-footer"></div>
          <div class="resize">
            <!-- icon-compress-alt -->
            <span
              @click="changeSize('increased')"
              style="color: rgba(70, 212, 255, 0.877)"
              :class="[
                'iconfont',
                fullScreenStatus.increased
                  ? 'icon-compress-alt'
                  : 'icon-expand-alt',
              ]"
            ></span>
          </div>
        </div>
        <div
          id="middle-bottom"
          :class="[fullScreenStatus.map ? 'fullscreen' : '']"
        >
          <!-- 热力图图表 -->
          <Map ref="map"></Map>
          <div class="resize">
            <!-- icon-compress-alt -->
            <span
              @click="changeSize('map')"
              style="color: rgba(41, 52, 65, 1)"
              :class="[
                'iconfont',
                fullScreenStatus.map ? 'icon-compress-alt' : 'icon-expand-alt',
              ]"
            ></span>
          </div>
        </div>
      </section>
      <section class="screen-right">
        <div
          id="right-top"
          :class="[fullScreenStatus.time ? 'fullscreen' : '']"
        >
          <!-- 违规事件发生在不同时段的占比图表 -->
          <Time ref="time"></Time>
          <div class="panel-footer"></div>
          <div class="resize">
            <!-- icon-compress-alt -->
            <span
              @click="changeSize('time')"
              style="color: rgba(70, 212, 255, 0.877)"
              :class="[
                'iconfont',
                fullScreenStatus.time ? 'icon-compress-alt' : 'icon-expand-alt',
              ]"
            ></span>
          </div>
        </div>
        <div
          id="right-bottom"
          :class="[fullScreenStatus.place ? 'fullscreen' : '']"
        >
          <!-- 违规事件高发街道图表 -->
          <Place ref="place"></Place>
          <div class="panel-footer"></div>
          <div class="resize">
            <!-- icon-compress-alt -->
            <span
              @click="changeSize('place')"
              style="color: rgba(70, 212, 255, 0.877)"
              :class="[
                'iconfont',
                fullScreenStatus.place
                  ? 'icon-compress-alt'
                  : 'icon-expand-alt',
              ]"
            ></span>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import DisposePercent from "@/components/DisposePercent";
import Increased from "@/components/Increased";
import Map from "@/components/Map";
import Place from "@/components/Place";
import Time from "@/components/Time";
import Today from "@/components/Today";
export default {
  data() {
    return {
      // 定义每一个图表的全屏状态
      fullScreenStatus: {
        disposePercent: false,
        increased: false,
        map: false,
        place: false,
        time: false,
        today: false,
      },
      gettime: null,
      t: null, // 定时器
    };
  },
  components: {
    DisposePercent,
    Increased,
    Map,
    Place,
    Time,
    Today,
  },
  created() {
    this.startTime();
  },
  methods: {
    startTime() {
      this.t = setTimeout(this.getCurrentTime, 1000); // 开始计时
    },
    getCurrentTime() {
      clearTimeout(this.t); // 清除定时器
      var _this = this;
      const yy = new Date().getFullYear();
      const mm = new Date().getMonth() + 1;
      const dd = new Date().getDate();
      const hh = new Date().getHours();
      const mf =
        new Date().getMinutes() < 10
          ? "0" + new Date().getMinutes()
          : new Date().getMinutes();
      const ss =
        new Date().getSeconds() < 10
          ? "0" + new Date().getSeconds()
          : new Date().getSeconds();
      _this.gettime =
        yy + "年" + mm + "月" + dd + "日 " + hh + ":" + mf + ":" + ss;
      this.t = setTimeout(this.getCurrentTime, 1000); // 设定定时器，循环运行
    },
    changeSize(chartName) {
      this.fullScreenStatus[chartName] = !this.fullScreenStatus[chartName];
      this.$nextTick(() => {
        this.$refs[chartName].screenAdapter();
      });
    },
  },
};
</script>
<style lang="less" scoped>
// 全屏样式的定义
.fullscreen {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  width: 100% !important;
  height: 100% !important;
  margin: 0 !important;
  z-index: 100;
  background: url(/static/img/bg.jpg) no-repeat top center !important;
}
.screen-container {
  width: 100%;
  height: 100%;
  padding: 0 20px;
  background: url(/static/img/bg.jpg) no-repeat top center;
  color: #fff;
  box-sizing: border-box;
}

.screen-header {
  width: 100%;
  height: 64px;
  font-size: 20px;
  position: relative;
  > div {
    img {
      width: 100%;
    }
  }
  .title {
    position: absolute;
    left: 50%;
    top: 50%;
    font-size: 25px;
    color: rgba(70, 212, 255, 0.877);
    font-weight: 700;
    transform: translate(-50%, -50%);
  }
  .title-left {
    display: flex;
    align-items: center;
    position: absolute;
    left: 0px;
    top: 50%;
    transform: translateY(-80%);
  }
  .title-right {
    display: flex;
    align-items: center;
    position: absolute;
    right: 0px;
    top: 50%;
    transform: translateY(-80%);
  }
  .datetime {
    font-size: 15px;
    margin-left: 10px;
    color: rgba(70, 212, 255, 0.932);
  }
}

.screen-body {
  width: 100%;
  height: 100%;
  display: flex;
  .screen-left {
    height: 100%;
    width: 27.6%;
    #left-top {
      height: 50%;
      position: relative;
      border: 1px solid rgba(25, 186, 139, 0.17);
      background: url(/static/img/line.png) rgba(255, 255, 255, 0.03);
    }
    #left-top::before {
      position: absolute;
      top: 0;
      left: 0;
      width: 10px;
      height: 10px;
      border-left: 2px solid #02a6b5;
      border-top: 2px solid #02a6b5;
      content: "";
    }
    #left-top::after {
      position: absolute;
      top: 0;
      right: 0;
      width: 10px;
      height: 10px;
      border-right: 2px solid #02a6b5;
      border-top: 2px solid #02a6b5;
      content: "";
    }
    #left-top .panel-footer {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
    }
    #left-top .panel-footer::before {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 10px;
      height: 10px;
      border-left: 2px solid #02a6b5;
      border-bottom: 2px solid #02a6b5;
      content: "";
    }
    #left-top .panel-footer::after {
      position: absolute;
      bottom: 0;
      right: 0;
      width: 10px;
      height: 10px;
      border-right: 2px solid #02a6b5;
      border-bottom: 2px solid #02a6b5;
      content: "";
    }
    #left-bottom {
      height: 35%;
      margin-top: 20px;
      position: relative;
      border: 1px solid rgba(25, 186, 139, 0.17);
      background: url(/static/img/line.png) rgba(255, 255, 255, 0.03);
    }
    #left-bottom::before {
      position: absolute;
      top: 0;
      left: 0;
      width: 10px;
      height: 10px;
      border-left: 2px solid #02a6b5;
      border-top: 2px solid #02a6b5;
      content: "";
    }
    #left-bottom::after {
      position: absolute;
      top: 0;
      right: 0;
      width: 10px;
      height: 10px;
      border-right: 2px solid #02a6b5;
      border-top: 2px solid #02a6b5;
      content: "";
    }
    #left-bottom .panel-footer {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
    }
    #left-bottom .panel-footer::before {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 10px;
      height: 10px;
      border-left: 2px solid #02a6b5;
      border-bottom: 2px solid #02a6b5;
      content: "";
    }
    #left-bottom .panel-footer::after {
      position: absolute;
      bottom: 0;
      right: 0;
      width: 10px;
      height: 10px;
      border-right: 2px solid #02a6b5;
      border-bottom: 2px solid #02a6b5;
      content: "";
    }
  }
  .screen-middle {
    height: 100%;
    width: 42.8%;
    margin-left: 1.5%;
    margin-right: 1.5%;
    #middle-top {
      width: 100%;
      height: 50%;
      position: relative;
      border: 1px solid rgba(25, 186, 139, 0.17);
      background: url(/static/img/line.png) rgba(255, 255, 255, 0.03);
    }
    #middle-top::before {
      position: absolute;
      top: 0;
      left: 0;
      width: 10px;
      height: 10px;
      border-left: 2px solid #02a6b5;
      border-top: 2px solid #02a6b5;
      content: "";
    }
    #middle-top::after {
      position: absolute;
      top: 0;
      right: 0;
      width: 10px;
      height: 10px;
      border-right: 2px solid #02a6b5;
      border-top: 2px solid #02a6b5;
      content: "";
    }
    #middle-top .panel-footer {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
    }
    #middle-top .panel-footer::before {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 10px;
      height: 10px;
      border-left: 2px solid #02a6b5;
      border-bottom: 2px solid #02a6b5;
      content: "";
    }
    #middle-top .panel-footer::after {
      position: absolute;
      bottom: 0;
      right: 0;
      width: 10px;
      height: 10px;
      border-right: 2px solid #02a6b5;
      border-bottom: 2px solid #02a6b5;
      content: "";
    }
    #middle-bottom {
      width: 100%;
      height: 38%;
      margin-top: 5px;
      position: relative;
    }
  }
  .screen-right {
    height: 100%;
    width: 27.6%;
    #right-top {
      height: 50%;
      position: relative;
      border: 1px solid rgba(25, 186, 139, 0.17);
      background: url(/static/img/line.png) rgba(255, 255, 255, 0.03);
    }
    #right-top::before {
      position: absolute;
      top: 0;
      left: 0;
      width: 10px;
      height: 10px;
      border-left: 2px solid #02a6b5;
      border-top: 2px solid #02a6b5;
      content: "";
    }
    #right-top::after {
      position: absolute;
      top: 0;
      right: 0;
      width: 10px;
      height: 10px;
      border-right: 2px solid #02a6b5;
      border-top: 2px solid #02a6b5;
      content: "";
    }
    #right-top .panel-footer {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
    }
    #right-top .panel-footer::before {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 10px;
      height: 10px;
      border-left: 2px solid #02a6b5;
      border-bottom: 2px solid #02a6b5;
      content: "";
    }
    #right-top .panel-footer::after {
      position: absolute;
      bottom: 0;
      right: 0;
      width: 10px;
      height: 10px;
      border-right: 2px solid #02a6b5;
      border-bottom: 2px solid #02a6b5;
      content: "";
    }
    #right-bottom {
      height: 35%;
      margin-top: 20px;
      position: relative;
      border: 1px solid rgba(25, 186, 139, 0.17);
      background: url(/static/img/line.png) rgba(255, 255, 255, 0.03);
    }
    #right-bottom::before {
      position: absolute;
      top: 0;
      left: 0;
      width: 10px;
      height: 10px;
      border-left: 2px solid #02a6b5;
      border-top: 2px solid #02a6b5;
      content: "";
    }
    #right-bottom::after {
      position: absolute;
      top: 0;
      right: 0;
      width: 10px;
      height: 10px;
      border-right: 2px solid #02a6b5;
      border-top: 2px solid #02a6b5;
      content: "";
    }
    #right-bottom .panel-footer {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
    }
    #right-bottom .panel-footer::before {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 10px;
      height: 10px;
      border-left: 2px solid #02a6b5;
      border-bottom: 2px solid #02a6b5;
      content: "";
    }
    #right-bottom .panel-footer::after {
      position: absolute;
      bottom: 0;
      right: 0;
      width: 10px;
      height: 10px;
      border-right: 2px solid #02a6b5;
      border-bottom: 2px solid #02a6b5;
      content: "";
    }
  }
}

.resize {
  position: absolute;
  right: 20px;
  top: 20px;
  cursor: pointer;
}
</style>
