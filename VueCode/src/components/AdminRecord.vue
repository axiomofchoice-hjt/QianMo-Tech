<template>
  <div class="xdisplay">
    <el-button
      type="primary"
      style="margin-top: 22px; position: absolute"
      size="small"
      @click="$router.push('/admin/record-new')"
      >添加违法事件</el-button
    >
    <div>
      <h2 style="text-align: center">违法记录</h2>
    </div>
    <!-- <el-button type="primary" @click="flush">刷新</el-button> -->
    <el-row>
      <el-col :span="12">
        <el-form label-width="200px">
          <el-form-item label="对日期筛选：">
            <el-date-picker
              v-model="filter.time"
              type="daterange"
              range-separator="至"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
              clearable
              :picker-options="timeFilterOptions"
              @change="filterChange"
            >
            </el-date-picker>
          </el-form-item>
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
      </el-col>
      <el-col :span="12">
        <el-form label-width="200px">
          <el-form-item label="对处理状态筛选：">
            <el-radio-group
              v-model="filter.states"
              @change="filterChange"
              :fill="filter.states === '全部' ? '#999' : '#409EFF'"
              size="small"
            >
              <el-radio-button
                v-for="item in tools.statesName"
                :key="item"
                :label="item"
              ></el-radio-button>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="对违法类型筛选：">
            <el-radio-group
              v-model="filter.illegal"
              @change="filterChange"
              :fill="filter.illegal === '全部' ? '#999' : '#409EFF'"
              size="small"
            >
              <el-radio-button
                v-for="item in tools.illegalName"
                :key="item"
                :label="item"
              ></el-radio-button>
            </el-radio-group>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
    <el-table
      :data="tableData"
      border
      :empty-text="querying ? '查询中' : '无数据'"
      style="width: 100%; margin-top: 10px"
    >
      <el-table-column prop="serial" label="事件编号"> </el-table-column>
      <el-table-column prop="formatTime" label="时间"> </el-table-column>
      <el-table-column prop="address" label="地点"> </el-table-column>
      <el-table-column prop="person" label="身份标志"> </el-table-column>
      <el-table-column prop="illegalCode" label="违法类型"> </el-table-column>
      <el-table-column prop="stateCode" label="处理状态"> </el-table-column>
      <el-table-column label="操作" width="143">
        　　　　<template slot-scope="scope">
          　　　　　　<el-button
            type="info"
            @click="check(scope.row.serial)"
            size="mini"
            style="margin-right: 10px"
            >查看</el-button
          >
          <template>
            <el-popconfirm title="删除这条记录？" @confirm="del(scope.row.serial)"
              ><el-button
                type="danger"
                size="mini"
                slot="reference"
                >删除</el-button
              >
            </el-popconfirm>
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
  </div>
</template>
<script>
import tools from "@/tools";
import dayjs from "dayjs";
export default {
  data() {
    return {
      timeFilterOptions: {
        shortcuts: [
          tools.RangeTimePickerShortcut("今天", 0, 0),
          tools.RangeTimePickerShortcut("昨天", 1, 1),
          tools.RangeTimePickerShortcut("最近三天", 3, 0),
          tools.RangeTimePickerShortcut("最近一周", 7, 0),
          tools.RangeTimePickerShortcut("最近两周", 14, 0),
          tools.RangeTimePickerShortcut("清除条件"),
        ],
      },
      tools,
      filter: {
        states: "全部",
        illegal: "全部",
        partition: "全部",
        time: null,
      },
      pagecount: 1,
      pageindex: 1,
      realpageindex: 1,
      tableData: [],
      cameraList: [],
      partitionList: [],
      querying: false,
    };
  },
  methods: {
    check(serial) {
      console.log(serial);
      this.$router.push(`/admin/record-check/${serial}`);
    },
    del(serial) {
      console.log(serial);
      this.clearTable();
      this.$http
        .post("/worker/delete", {
          serial,
        })
        .then(() => {
          this.init();
        });
    },
    filterChange() {
      // console.log(this.filter.time);
      this.$router.push(
        `/admin/record/${this.getTimeStr()}${tools.statesName.indexOf(
          this.filter.states
        )}/${tools.illegalName.indexOf(this.filter.illegal)}/${
          this.filter.partition
        }/1`
      );
    },
    changepageindex(pageindex) {
      this.$router.push(
        `/admin/record/${this.getTimeStr()}${tools.statesName.indexOf(
          this.filter.states
        )}/${tools.illegalName.indexOf(this.filter.illegal)}/${
          this.filter.partition
        }/${pageindex}`
      );
    },
    flush() {
      console.log("flush");
      console.log(this.filter.states);
      console.log(this.$route.params.state === "number");
      var query = {
        pagesize: 5,
        pageIndex: this.pageindex,
        timeOrder: "DESC",
      };
      if (this.filter.time !== null) {
        Object.defineProperty(query, "from_time", {
          value: dayjs(this.filter.time[0]).utc().format("YYYY-MM-DD HH:mm:ss"),
          enumerable: true,
        });
        Object.defineProperty(query, "to_time", {
          value: dayjs(this.filter.time[1]).utc().format("YYYY-MM-DD HH:mm:ss"),
          enumerable: true,
        });
      }
      if (this.filter.states !== "全部") {
        Object.defineProperty(query, "states", {
          value: "" + tools.statesName.indexOf(this.filter.states),
          enumerable: true,
        });
      }
      if (this.filter.illegal !== "全部") {
        Object.defineProperty(query, "illegal_nature", {
          value: "" + tools.illegalName.indexOf(this.filter.illegal),
          enumerable: true,
        });
      }
      if (this.filter.partition !== "全部") {
        Object.defineProperty(query, "partition", {
          value: this.filter.partition,
          enumerable: true,
        });
      }
      console.log("query:", query);
      this.clearTable();
      this.$http.post("/worker/show_illegal", query).then((response) => {
        console.log("response:", response.data);
        let content = response.data.data.content;
        let labels = response.data.data.labels;
        this.tableData = tools.trans(labels, content, tools.illegalNameMap);
        this.pagecount = response.data.page;
        // console.log(this.pagecount);

        for (let i of this.tableData) {
          tools.illegalElementExtend(i);
        }
        console.log(this.tableData);
        this.realpageindex = this.pageindex;
        this.querying = false;
      });
    },
    init() {
      this.filter.states =
        tools.statesName[tools.intParams(this.$route.params.state)];
      this.filter.illegal =
        tools.illegalName[tools.intParams(this.$route.params.illegal)];
      this.filter.partition =
        typeof this.$route.params.partition === "string"
          ? this.$route.params.partition
          : "全部";
      this.filter.time =
        typeof this.$route.params.date1 === "string"
          ? [
              dayjs(this.$route.params.date1).toDate(),
              dayjs(this.$route.params.date2).toDate(),
            ]
          : null;
      this.pageindex = Math.max(
        1,
        tools.intParams(this.$route.params.pageindex)
      );
      this.cameraUpdate();
      this.flush();
    },
    cameraUpdate() {
      tools.getCameraList(this.$http, (list) => {
        this.cameraList = list;
        this.partitionList = tools.collectAttr(list, "partition");
      });
    },
    clearTable() {
      this.tableData = [];
      this.querying = true;
      // this.pagecount = 1;
    },
    getTimeStr() {
      if (this.filter.time !== null) {
        return `${dayjs(this.filter.time[0]).startOf("date").toJSON()}/${dayjs(
          this.filter.time[1]
        )
          .startOf("date")
          .add(1, "day")
          .subtract(1, "second")
          .toJSON()}/`;
      } else {
        return "";
      }
    },
  },
  created() {
    this.init();
  },
  watch: {
    $route() {
      this.init();
    },
  },
};
</script>
