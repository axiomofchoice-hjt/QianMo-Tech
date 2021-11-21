<template>
    <div class="com-container">
        <div class="title" :style="comStyle">
            <span>{{'┃ ' + showTitle}}</span>
            <span class="iconfont title-icon" :style="comStyle" @click="showChoice = !showChoice">&#xe6eb;</span>
            <div class="select-con" v-show="showChoice" :style="marginStyle">
                <div class="select-item" v-for="item in selectTypes" :key="item.key" @click="handleSelect(item.key)">
                    {{item.text}}
                </div>
            </div>
        </div>
        <div class="com-chart" ref="increased_ref"></div>
    </div>
</template>

<script>
import chalk from '../../public/static/theme/chalk'
export default {
    data () {
        return {
            chartInstance: null,
            allData: null,
            showChoice: false, // 是否选择可选项
            choiceType: 'helmet', // 显示的数据类型
            titleFontSize: 0, // 指明标题的字体大小
            getTimerID: null // 请求后端定时器
        }
    },
    created () {
        this.$socket.registerCallBack('increasedData', this.getData)
    },
    mounted () {
        this.initChart()
        // this.getData()
        this.getTimerID = setInterval(() => {
            setTimeout(
                this.$socket.send({
                    action: 'getData',
                    socketType: 'increasedData',
                    chartName: 'increased',
                    value: ''
                }), 0)
        }, 1000)
        window.addEventListener('resize', this.screenAdapter)
        this.screenAdapter()
    },
    destroyed () {
        clearInterval(this.getTimerID)
        window.removeEventListener('resize', this.screenAdapter)
        this.$socket.unRegisterCallBack('increasedData')
    },
    computed: {
        selectTypes () {
            if (!this.allData) {
                return []
            } else {
                return this.allData.type.filter(item => {
                    return item.key !== this.choiceType
                })
            }
        },
        showTitle () {
            if (!this.allData) {
                return []
            } else {
                return this.allData[this.choiceType].title
            }
        },
        // 设置给标题的样式
        comStyle () {
            return {
                fontSize: this.titleFontSize + 'px'
            }
        },
        marginStyle () {
            return {
                marginLeft: this.titleFontSize * 2 + 'px'
            }
        }
    },
    methods: {
        initChart () {
           this.chartInstance = this.$echarts.init(this.$refs.increased_ref,'chalk')
           const initOption = {
               grid: {
                   left: '3%',
                   top: '35%',
                   right: '4%',
                   bottom: '1%',
                   containLabel: true
               },
               tooltip: {
                   trigger: 'axis'
               },
               legend: {
                   left: 20,
                   top: '15%',
                   icon: 'circle'
               },
               xAxis: {
                   type: 'category',
                   boundaryGap: false
                },
               yAxis: {
                    type: 'value'
                }
           }
           this.chartInstance.setOption(initOption)
        },
        getData (ret) {
            // const ret = await this.$http.get('increased')
            // console.log(ret)
            this.allData = ret
            console.log(this.allData)
            this.updateChart()
        },
        updateChart () {
            // 半透明的颜色值
            const colorArr1 = [
                'rgb(11, 168, 44)', // 深绿
                'rgb(44, 110, 255)', // 深蓝
                'rgb(244, 204, 204)', // 肉粉
                'rgb(255, 0, 0)', // 红
                'rgb(250, 105, 0)', // 橙
                'rgb(255, 0, 255)', // 粉紫
                'rgb(230, 255, 0)', // 亮黄
                'rgb(153, 0, 255)', // 紫
                'rgb(0, 213, 255)', // 天蓝
                'rgb(0, 255, 34)' // 亮绿
            ]
            // 全透明的颜色值
            const colorArr2 = [
                'rgba(11, 168, 44, 0)', // 深绿
                'rgba(44, 110, 255, 0)', // 深蓝
                'rgba(244, 204, 204, 0)', // 肉粉
                'rgba(255, 0, 0, 0)', // 红
                'rgba(250, 105, 0, 0)', // 橙
                'rgba(255, 0, 255, 0)', // 粉紫
                'rgba(230, 255, 0, 0)', // 亮黄
                'rgba(153, 0, 255, 0)', // 紫
                'rgba(0, 213, 255, 0)', // 天蓝
                'rgba(0, 255, 34, 0)' // 亮绿
            ]
            const timeArr = this.allData.common.day
            const valueArr = this.allData[this.choiceType].data
            const seriesArr = valueArr.map((item, index) => {
                return {
                    name: item.name,
                    type: 'line',
                    data: item.data,
                    stack: this.choiceType,
                    color: colorArr1[index],
                    areaStyle: {
                        color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                            {
                                offset: 0,
                                color: colorArr1[index]
                            }, // 0%的颜色值
                            {
                                offset: 1,
                                color: colorArr2[index]
                            } // 100%的颜色值
                        ])
                    },
                    itemStyle: {
                        normal: {
                            lineStyle: {
                                color: colorArr1[index]
                            }
                        }
                    }
                }
            })
            // 图例的数据
            const legendArr = valueArr.map((item) => {
                return item.name
            })
            const dataOption = {
                xAxis: {
                    data: timeArr
                },
                legend: {
                    data: legendArr
                },
                series: seriesArr

            }
            this.chartInstance.setOption(dataOption)
        },
        screenAdapter () {
            this.titleFontSize = this.$refs.increased_ref.offsetWidth / 100 * 1.8
            const adapterOption = {
                legend: {
                    itemWidth: this.titleFontSize,
                    itemHeight: this.titleFontSize * 2,
                    itemGap: this.titleFontSize,
                    textStyle: {
                        fontSize: this.titleFontSize * 1.5
                    },
                    padding: [this.titleFontSize, this.titleFontSize * 2, 0, 0]
                }
            }
            this.chartInstance.setOption(adapterOption)
            this.chartInstance.resize()
        },
        handleSelect (currentType) {
            this.choiceType = currentType
            this.updateChart()
            this.showChoice = false
        }
    }
}
</script>

<style lang="less" scoped>
.title {
    position: absolute;
    left: 20px;
    top: 20px;
    color: rgba(70, 212, 255, 0.877);
    z-index: 10;
    font-weight: 700;
    .title-icon {
        // margin-left: 10px;
        cursor: pointer;
    }
    .select-con {
        background-color: rgb(12, 17, 75);
    }
    .select-item {
        cursor: pointer;
        font-weight: 700;
    }
}
</style>
