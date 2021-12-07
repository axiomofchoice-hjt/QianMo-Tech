<template>
  <div class="xdisplay">
    <!-- <el-button
      type="primary"
      style="margin-top: 22px"
      size="small"
      @click="$router.push('/admin/record/new')"
      >添加摄像头</el-button
    > -->
    <h2 style="text-align: center">摄像头管理</h2>
    <el-row>
      <el-col :span="8">
        <el-form label-width="130px">
          <el-form-item label="对分区筛选：">
            <el-select
              v-model="filter.partition"
              filterable
              placeholder="请选择"
              @change="filterChange"
            >
              <el-option label="全部" value="全部"></el-option>
              <el-option
                v-for="item in partitionList"
                :key="item"
                :label="item"
                :value="item"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <el-table
          :data="cameraList"
          border
          :empty-text="querying ? '查询中' : '无数据'"
          style="width: 100%; margin-top: 10px"
        >
          <el-table-column prop="cameraId" label="摄像头编号">
          </el-table-column>
          <!-- <el-table-column prop="partition" label="分区"> </el-table-column> -->
          <el-table-column prop="address" label="地点"> </el-table-column>
          <!-- <el-table-column prop="model" label="型号"> </el-table-column>
          <el-table-column prop="point" label="坐标"> </el-table-column> -->
          <el-table-column prop="state" label="状态"> </el-table-column>
          <el-table-column label="操作" width="77">
            　　　　<template slot-scope="scope">
            <template v-if="scope.row.cameraId !== cameraObject.cameraId">
              　　　　　　<el-button
                type="info"
                @click="check(scope.row.cameraId)"
                size="mini"
                >查看</el-button
              >
            </template>
            <template v-else>
              <div style="text-align: center;">
              查看中
              </div>
            </template>
              　　　　</template
            >
          </el-table-column>
        </el-table>
        <div v-if="!querying" class="block">
          <el-pagination
            layout="prev, pager, next"
            :page-count="pagecount"
            :current-page="realpageindex"
            @current-change="changepageindex"
            :disabled="querying"
          >
          </el-pagination>
        </div>
      </el-col>
      <el-col :span="16">
        <LivePlayer :videoUrl="videoUrl" ref="player" live style="margin: 20px 50px;"/>
        <div style="text-align: center; margin-top: 10px">{{cameraObject.cameraId}} {{cameraObject.address}}</div>
        <div style="text-align: right; margin: 10px 50px;"><router-link to="/admin/camera-draw">画停车线</router-link></div>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import tools from "@/tools";
import LivePlayer from '@liveqing/liveplayer'
export default {
  components: {
      LivePlayer
  },
  data() {
    return {
      filter: {
        partition: "全部",
      },
      pagecount: 1,
      pageindex: 1,
      realpageindex: 1,
      allCameralist: [],
      cameraList: [],
      cameraObject: {
        cameraId: "",
        address: ""
      },
      partitionList: [],
      querying: false,
      videoUrl: '',
    };
  },
  methods: {
    check(cameraId) {
      console.log(cameraId);
      this.$router.push(`/admin/camera/${this.filter.partition}/${this.pageindex}/${cameraId}`);
    },
    filterChange() {
      // console.log(this.filter.time);
      this.$router.push(`/admin/camera/${this.filter.partition}/1/${this.cameraObject.cameraId}`);
    },
    changepageindex(pageindex) {
      this.$router.push(`/admin/camera/${this.filter.partition}/${pageindex}/${this.cameraObject.cameraId}`);
    },
    init() {
      this.query();
    },
    update() {
      this.filter.partition =
        typeof this.$route.params.partition === "string"
          ? this.$route.params.partition
          : "全部";
      this.pageindex = Math.max(
        1,
        tools.intParams(this.$route.params.pageindex)
      );
      this.cameraList = [];
      this.partitionList = tools.collectAttr(this.allCameralist, "partition");
      this.querying = false;
      for (let i of this.allCameralist) {
        if (
          this.filter.partition === "全部" ||
          this.filter.partition === i.partition
        ) {
          this.cameraList.push(i);
        }
      }
      var pagesize = 5;
      this.pagecount = Math.ceil(this.cameraList.length / pagesize);
      this.cameraList = this.cameraList.slice(
        (this.pageindex - 1) * pagesize,
        this.pageindex * pagesize
      );
      this.realpageindex = this.pageindex;
      if (typeof this.$route.params.cameraId === "string") {
        for (let i of this.allCameralist) if (i.cameraId === this.$route.params.cameraId) this.cameraObject = i;
      } else {
        this.cameraObject = this.allCameralist[0];
      }
      if (this.cameraObject.cameraId === 'JM20211103001')
        this.videoUrl = "video.mp4";
      else
        this.videoUrl = '';
    },
    query() {
      tools.getCameraList(this.$http, (list) => {
        this.allCameralist = list;
        this.update();
      });
    },
    // clearTable() {
    //   this.cameraList = [];
    //   this.querying = true;
    //   // this.pagecount = 1;
    // },
  },
  created() {
    this.init();
  },
  watch: {
    $route() {
      this.update();
    },
  },
};
</script>
