<template>
  <div class="com-container">
        <div class="com-chart" ref="today_ref"></div>
  </div>
</template>

<script>
import chalk from '../../public/static/theme/chalk'
export default {
    data () {
        return {
            chartInstance: null,
            allData: null,
            getTimerID: null
        }
    },
    created () {
        this.$socket.registerCallBack('todayData', this.getData)
    },
    mounted () {
        this.initChart()
        // this.getData()
        this.getTimerID = setInterval(() => {
            setTimeout(
                this.$socket.send({
                    action: 'getData',
                    socketType: 'todayData',
                    chartName: 'today',
                    value: ''
                }), 0)
        }, 1000)
        window.addEventListener('resize', this.screenAdapter)
        this.screenAdapter()
    },
    destroyed () {
        window.removeEventListener('resize', this.screenAdapter)
        this.$socket.unRegisterCallBack('todayData')
        clearInterval(this.getTimerID)
    },
    methods: {
        initChart () {
            this.chartInstance = this.$echarts.init(this.$refs.today_ref,'chalk')
            const initOption = {
                title: {
                    text: '┃ 今日违规行驶的人次',
                    left: 20,
                    top: 20
                },
                series: [{
                    type: 'gauge',
                    min: 0,
                    max: 1000,
                    axisLine: {
                        show: true,
                        lineStyle: {
                            color: [
                                [0.25, '#14D06C'],
                                [0.5, '#A9DD2B'],
                                [0.75, '#F0D025'],
                                [1, '#FC3340']
                            ],
                            width: 25// 表盘宽度
                        }
					},
                    pointer: {
                        length: '60%'
                    }
                }]
            }
            this.chartInstance.setOption(initOption)
        },
        getData (ret) {
            // const ret = await this.$http.get ('today')
            this.allData = ret
            console.log(ret)
            this.updateChart()
        },
        updateChart () {
            const dataOption = {
                series: [
                    {
                        data: [{
                            value: this.allData[0].value
                        }]
                    }
                ]
            }
            this.chartInstance.setOption(dataOption)
        },
        screenAdapter () {
            const titleFontSize = this.$refs.today_ref.offsetWidth / 100 * 3.6
            const adapterOption = {
                title: {
                    textStyle: {
                        fontSize: titleFontSize
                    }
                },
                series: [
                    {
                        radius: titleFontSize * 7,
                        center: ['50%', '60%'],
                        axisLabel: {
                            fontSize: titleFontSize / 1.5
                        },
                        detail: {
                            fontSize: titleFontSize,
                            fontWeight: 'bold'
                        },
                        pointer: {
                            width: titleFontSize / 5
                        }
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
