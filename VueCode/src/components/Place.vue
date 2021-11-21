<template>
  <div class="com-container">
        <div class="com-chart" ref="place_ref"></div>
  </div>
</template>

<script>
import chalk from '../../public/static/theme/chalk'
export default {
    data () {
        return {
            chartInstance: null,
            allData: null,
            startValue: 0, // 区域缩放的起点值
            endValue: 9, // 区域缩放的终点值
            timerId: null,
            getTimerID: null
        }
    },
    created () {
        this.$socket.registerCallBack('placeData', this.getData)
    },
    mounted () {
        this.initChart()
        this.$socket.send({
            action: 'getData',
            socketType: 'placeData',
            chartName: 'place',
            value: ''
        })
        // this.getData()
        this.getTimerID = setInterval(() => {
            setTimeout(
                this.$socket.send({
                    action: 'getData',
                    socketType: 'placeData',
                    chartName: 'place',
                    value: ''
                }), 0)
        }, 60000)
        window.addEventListener('resize', this.screenAdapter)
        this.screenAdapter()
    },
    destroyed () {
        clearInterval(this.timerId)
        clearInterval(this.getTimerID)
        window.removeEventListener('resize', this.screenAdapter)
        this.$socket.unRegisterCallBack('placeData')
    },
    methods: {
        initChart () {
            this.chartInstance = this.$echarts.init(this.$refs.place_ref,'chalk')
            const initOption = {
                title: {
                    text: '┃ 违规事件高发街道',
                    left: 20,
                    top: 20
                },
                grid: {
                    top: '40%',
                    left: '10%',
                    right: '5%',
                    bottom: '5%',
                    containLabel: true
                },
                tooltip: {
                    show:true
                },
                xAxis: {
                    type: 'category',
                    axisLabel: {  
                        interval:0,  
                        rotate:40  
                    }
                },
                yAxis: {
                    type: 'value',
                    // 坐标轴刻度
                    axisTick: {
                        show: false
                    },
                    // 坐标轴轴线
                    axisLine: {
                        show: false
                    },
                    // 坐标轴在图表区域中的分隔线
                    splitLine: {
                        show: false
                    },
                    // 坐标轴刻度标签
                    axisLabel: {
                        show: false
                    }
                },
                series: [
                    {
                        type: 'bar'
                    }
                ]
            }
            this.chartInstance.setOption(initOption)
            this.chartInstance.on('mouseover', () => {
                clearInterval(this.timerId)
            })
            this.chartInstance.on('mouseout', () => {
                this.startInterval()
            })
        },
        getData (ret) {
            // const ret = await this.$http('place')
            this.allData = ret
            this.allData.sort((a, b) => {
                return b.value - a.value
            })
            console.log(this.allData)
            this.updateChart()
            this.startInterval()
        },
        updateChart () {
            const colorArr = [
                ['#0BA82C', '#4FF778'],
                ['#2E72BF', '#23E5E5'],
                ['#5052EE', '#AB6EE5']
            ]
            const placeArr = this.allData.map(item => {
                return item.name
            })
            const valueArr = this.allData.map(item => {
                return item.value
            })
            const dataOption = {
                xAxis: {
                    data: placeArr
                },
                dataZoom: {
                    show: false,
                    startValue: this.startValue,
                    endValue: this.endValue
                },
                series: [
                    {
                        data: valueArr,
                        itemStyle: {
                            color: arg => {
                                let targetColorArr = null
                                if (arg.value > 300) {
                                    targetColorArr = colorArr[0]
                                    return new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                        {
                                            offset: 0,
                                            color: targetColorArr[0]
                                        },
                                        {
                                            offset: 1,
                                            color:targetColorArr[1]
                                        }
                                    ])
                                } else if (arg.value > 200) {
                                    targetColorArr = colorArr[1]
                                    return new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                        {
                                            offset: 0,
                                            color: targetColorArr[0]
                                        },
                                        {
                                            offset: 1,
                                            color:targetColorArr[1]
                                        }
                                    ])
                                } else {
                                    targetColorArr = colorArr[2]
                                    return new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                        {
                                            offset: 0,
                                            color: targetColorArr[0]
                                        },
                                        {
                                            offset: 1,
                                            color:targetColorArr[1]
                                        }
                                    ])
                                }
                            }
                        }
                    }
                ]
            }
            this.chartInstance.setOption(dataOption)
        },
        screenAdapter () {
            const titleFontSize = this.$refs.place_ref.offsetWidth / 100 * 3.6
            const adapterOption = {
                title: {
                    textStyle: {
                        fontSize: titleFontSize
                    }
                },
                series: [
                    {
                        barWidth: titleFontSize,
                        itemStyle: {
                            barBorderRadius: [titleFontSize / 2, titleFontSize / 2, 0, 0]
                        }
                    }
                ]
            }
            this.chartInstance.setOption(adapterOption)
            this.chartInstance.resize()
        },
        startInterval () {
            if (this.timerId) {
                clearInterval(this.timerId)
            }
            this.timerId = setInterval(() => {
                this.startValue++
                this.endValue++
                if (this.endValue > this.allData.length - 1) {
                    this.startValue = 0
                    this.endValue = 9
                }
                this.updateChart()
            }, 2000)
        }
    }
}
</script>

<style lang="less" scoped>
</style>
