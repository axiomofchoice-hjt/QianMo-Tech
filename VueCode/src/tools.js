import dayjs from 'dayjs';
export default {
  statesName: ["全部", "未处理", "已处理", "申诉中"],
  illegalName: ["全部", "闯红灯", "逆行", "未戴头盔"],
  illegalNameMap: {
    事件编号: "serial",
    违法性质: "illegalnature",
    时间: "time",

    分区: "partition",
    街道: "street",
    地点: "address",
    坐标: "point",

    处理结果: "states",
    处理者: "handler",
    违规证明: "record",

    身份证: "identity",
    车牌: "carplate",
  },
  cameraNameMap: {
    摄像头编号: "cameraId",
    添加时间: "addTime",
    型号: "model",
    坐标: "point",
    分区: "partition",
    街道: "street",
    地点: "address",
    状态: "state"
  },
  trans(labels, content, nameMap) {
    var result = [];
    for (let i of content) {
      var rec = {};
      for (let j = 0; j < labels.length; j++) {
        rec[nameMap[labels[j]]] = i[j];
      }
      rec.id = result.length;
      result.push(rec);
    }
    return result;
  },
  uniqued(list) {
    return Array.from(new Set(list));
  },
  collectAttr(list, attr) {
    var result = [];
    console.log("collect:", list);
    for (let i of list) result.push(i[attr]);
    return this.uniqued(result);
  },
  intParams(s) {
    return (typeof s === 'string' ? parseInt(s) : 0);
  },
  getCameraList(http, func) {
    http.post("/camera/show_camera", {
      "pagesize": 100000,
      "pageIndex": 1
    }).then((response) => {
      // console.log(response);
      var labels = response.data.data.labels;
      var content = response.data.data.content;
      var list = this.trans(labels, content, this.cameraNameMap);
      // console.log(list);
      func(list);
    });
  },
  illegalElementExtend(rec) {
    rec.illegalList = [];
    for (let j of rec.illegalnature.split(","))
      rec.illegalList.push(this.illegalName[j]);
    rec.illegalCode = rec.illegalList.join(", ");
    rec.stateCode = this.statesName[rec.states];
    rec.person = rec.identity + " / " + rec.carplate;
    rec.formatTime = dayjs(rec.time).format("YYYY-MM-DD HH:mm:ss");
    rec.pictures = rec.record.split(' ');
  },
  RangeTimePickerShortcut(text, day1, day2) {
    if (day1 === undefined) {
      return {
        text: text,
        onClick(picker) {
          picker.$emit("pick", null);
        },
      };
    }
    return {
      text: text,
      onClick(picker) {
        picker.$emit("pick", [
          dayjs().subtract(day1, "day").toDate(),
          dayjs().subtract(day2, "day").toDate(),
        ]);
      },
    };
  },
  blobToFile(blob, fileName) {
    return new File([blob], fileName);
  },
};