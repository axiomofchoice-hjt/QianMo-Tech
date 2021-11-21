<template>
  <div class="com-container">
        <div class="com-chart" ref="time_ref"></div>
  </div>
</template>

<script>
import chalk from '../../public/static/theme/chalk'
export default {
    data () {
        return {
            chartInstance: null,
            allData: null,
             getTimerID: null // 请求后端定时器
        }
    },
    created () {
        this.$socket.registerCallBack('timeData', this.getData)
    },
    mounted () {
        this.initChart()
        // this.getData()
        this.getTimerID = setInterval(() => {
            setTimeout(
                this.$socket.send({
                    action: 'getData',
                    socketType: 'timeData',
                    chartName: 'time',
                    value: ''
                }), 0)
        }, 1000)
        window.addEventListener('resize', this.screenAdapter)
        this.screenAdapter()
    },
    destroyed () {
        window.removeEventListener('resize', this.screenAdapter)
        this.$socket.unRegisterCallBack('timeData')
        clearInterval(this.getTimerID)
    },
    methods: {
        initChart () {
            this.chartInstance = this.$echarts.init(this.$refs.time_ref,'chalk')
            const initOption = {
                title: {
                    text: '┃ 违规事件发生在不同时段的占比',
                    left: 20,
                    top: 20
                },
                legend: {
                    top: '12%',
                    left: '10%',
                    icon: 'circle'
                },
                tooltip: {
                    show: true,
                    formatter: arg => {
                        let retStr = ''
                        retStr += `
                        ${arg.name + '违规人数占比' + arg.percent + '%'}
                        `
                        return retStr
                    }
                },
                series: [
                    {
                        type: 'pie',
                        emphasis: {
                            label: {
                                show: true
                            },
                            labelLine: {
                                show: true
                            }
                        },
                        roseType: 'radius',
                        center: ['50%','70%']
                    }
                ]
            }
            this.chartInstance.setOption(initOption)
        },
        getData (ret) {
            // const ret = await this.$http.get ('time')
            this.allData = ret
            console.log(this.allData)
            this.updateChart()
        },
        updateChart () {
            const colorArr = [
                'rgb(11, 168, 44)', // 深绿
                'rgb(44, 110, 255)', // 深蓝
                'rgb(0,255,255)', // 天蓝
                'rgb(255, 0, 0)', // 红
                'rgb(230, 255, 0)', // 亮黄
                'rgb(153, 0, 255)' // 紫
            ]
            const legendData = this.allData.map(item => {
                return item.name
            })
            const seriesData = this.allData.map(item => {
                return {
                    name: item.name,
                    value: item.value === '0' ? null : item.value
                }
            })
            const dataOption = {
                legend: {
                    data: legendData
                },
                series: [
                    {
                        color: colorArr,
                        data: seriesData
                    }
                ]
            }
            this.chartInstance.setOption(dataOption)
        },
        screenAdapter () {
            const titleFontSize = this.$refs.time_ref.offsetWidth / 100 * 3.6
            const adapterOption = {
                title: {
                    textStyle: {
                        fontSize: titleFontSize
                    }
                },
                legend: {
                    itemWidth: titleFontSize,
                    itemHeight: titleFontSize * 1.2,
                    itemGap: titleFontSize,
                    textStyle: {
                        fontSize: titleFontSize / 1.2
                    }
                },
                series: [
                    {
                        radius: titleFontSize * 3.7
                    }
                ]
            }
            this.chartInstance.setOption(adapterOption)
            this.chartInstance.resize()
        }
    }
}
</script>

<style lang="less" scoped>
</style>
