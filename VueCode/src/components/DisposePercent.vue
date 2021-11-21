<!--
各个地点的已处理事件vs未处理事件的横向柱状图
上城区，下城区，江干区，拱墅区，西湖区，滨江区，萧山区，余杭区，富阳区，临安区
-->
<template>
    <div class="com-container">
        <div class="com-chart" ref="disposepercent_ref"></div>
    </div>
</template>

<script>
import chalk from '../../public/static/theme/chalk'
export default {
    data () {
        return {
            chartInstance: null,
            allData: null, // 服务器返回的数据
            showData: null,
            disposedData: null,
            undisposedData: null,
            currentPage: 1, // 当前显示的页数
            totalPage: 0, // 一共有多少页
            timerID: null, // 定时器标识
            getTimerID: null // 请求后端定时器
        }
    },
    created () {
        this.$socket.registerCallBack('disposePercentData', this.getData)
    },
    mounted () {
        this.initChart()
        // this.getData()
        this.$socket.send({
            action: 'getData',
            socketType: 'disposePercentData',
            chartName: 'disposepercent',
            value: ''
        })
        this.getTimerID = setInterval(() => {
            setTimeout(
                this.$socket.send({
                    action: 'getData',
                    socketType: 'disposePercentData',
                    chartName: 'disposepercent',
                    value: ''
                }), 0)
        }, 6000)
        window.addEventListener('resize', this.screenAdapter)
        // 在页面加载完成的时候，主动进行屏幕的适配
        this.screenAdapter()
    },
    destroyed () {
        clearInterval(this.timerID)
        clearInterval(this.getTimerID)
        // 在组件销毁的时候，需要将监听器取消掉
        window.removeEventListener('resize', this.screenAdapter)
        this.$socket.unRegisterCallBack('disposePercentData')
    },
    methods: {
        // 初始化echartsInstance对象
        initChart () {
            this.chartInstance = this.$echarts.init(this.$refs.disposepercent_ref,'chalk')
            // 对图表初始化配置的控制
            const initOption = {
                title: {
                    text: '┃ 各个市区违规事件处理率',
                    left: 20,
                    top: 20
                },
                legend: {
                    data: ['已处理', '未处理'],
                    left: '65%',
                    top: '13%'
                },
                grid: {
                    top: '20%',
                    left: '3%',
                    right: '6%',
                    bottom: '3%',
                    containLabel: true // 距离是包含坐标轴上的文字
                },
                xAxis: {
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
                yAxis: {
                    type: 'category',
                    // 坐标轴轴线
                    axisLine: {
                        show: false
                    }
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'none'
                    },
                    formatter: arg => {
                        let retStr = ''
                        if (arg[0].value === 0) {
                            retStr += `${arg[1].seriesName + ':' + arg[1].value + '%'}`
                        } else if (arg[1].value === 0) {
                            retStr += `${arg[0].seriesName + ':' + arg[0].value + '%'}`
                        } else {
                            retStr += `
                                <div>${arg[0].seriesName + ':' + arg[0].value + '%'}</div>
                                <div>${arg[1].seriesName + ':' + arg[1].value + '%'}</div>
                            `
                        }
                        return retStr
                    }
                },
                series: [
                    {
                        type: 'bar',
                        stack: 'total',
                        name: '已处理', // 系列名称, 用于tooltip的显示, legend 的图例筛选
                        label: {
                            show: false,
                            formatter: arg => {
                                if (arg.data) {
                                    return arg.data + '%'
                                }
                            },
                            textStyle: {
                                color: 'white'
                            }
                        },
                        itemStyle: {
                            color: '#AB6EE5'
                        }
                    },
                    {
                        type: 'bar',
                        stack: 'total',
                        name: '未处理',
                        label: {
                            show: false,
                            formatter: arg => {
                                if (arg.data) {
                                    return arg.data + '%'
                                }
                            },
                            textStyle: {
                                color: 'white'
                            }
                        },
                        itemStyle: {
                            color: '#5052EE'
                        }
                    }
                ]
            }
            this.chartInstance.setOption(initOption)
            // 对图标对象进行鼠标事件的监听
            this.chartInstance.on('mouseover', () => {
                clearInterval(this.timerID)
            })
            this.chartInstance.on('mouseout', () => {
                this.startInterval()
            })
        },
        getData (ret) {
            // http:localhost/8888/api/disposepercent
            // const ret = await this.$http.get('disposepercent')
            this.allData = ret
            console.log(this.allData)
            // 对数据排序
            this.allData.sort((a, b) => {
                return (a.disposed / (a.disposed + a.undisposed) - b.disposed / (b.disposed + b.undisposed))
            })
            // 每五个元素显示一页
            this.totalPage = this.allData.length % 5 === 0 ? this.allData.length / 5 : this.allData.length / 5 + 1
            // console.log(this.totalPage)
            this.updateChart()
            // 启动定时器
            this.startInterval()
        },
        // 更新图表
        updateChart () {
            const start = (this.currentPage - 1) * 5
            const end = this.currentPage * 5
            this.showData = this.allData.slice(start, end)
            const areaNames = this.showData.map((item) => {
                return item.name
            })
            this.disposedData = this.showData.map((item) => {
                var total = item.disposed + item.undisposed
                return (Math.round(item.disposed / total * 10000) / 100.00)
            })
            this.undisposedData = this.showData.map((item) => {
                var total = item.disposed + item.undisposed
                return (Math.round(item.undisposed / total * 10000) / 100.00)
            })
            for (var i = 0; i < this.showData.length; i++) {
                if (this.disposedData[i] === 0) {
                    this.undisposedData[i] = {
                        value: this.undisposedData[i],
                        itemStyle: {
                            barBorderRadius: [this.getRadius(), this.getRadius(), this.getRadius(), this.getRadius()]
                        }
                    }
                } else if (this.undisposedData[i] === 0) {
                    this.disposedData[i] = {
                        value: this.disposedData[i],
                        itemStyle: {
                            barBorderRadius: [this.getRadius(), this.getRadius(), this.getRadius(), this.getRadius()]
                        }
                    }
                }
            }
            const dataOption = {
                yAxis: {
                    data: areaNames
                },
                series: [
                    {
                        data: this.disposedData
                    },
                    {
                        data: this.undisposedData
                    }
                ]
            }
            this.chartInstance.setOption(dataOption)
        },
        getRadius () {
            const titleFontSize = this.$refs.disposepercent_ref.offsetWidth / 100 * 3.6
            return titleFontSize / 0.6
        },
        // 启动定时器
        startInterval () {
            if (this.timerID) {
                clearInterval(this.timerID)
            }
            this.timerID = setInterval(() => {
                this.currentPage++
                if (this.currentPage > this.totalPage) {
                    this.currentPage = 1
                }
                this.updateChart()
            }, 3000)
        },
        // 当浏览器的大小发生变化的时候会调用的方法，完成屏幕的适配
        screenAdapter () {
            // console.log(this.$refs.disposepercent_ref.offsetWidth)
            const titleFontSize = this.$refs.disposepercent_ref.offsetWidth / 100 * 3.6
            // 和分辨率大小相关的配置项
            const adapterOption = {
                title: {
                    textStyle: {
                        fontSize: titleFontSize
                    }
                },
                legend: {
                    itemWidth: titleFontSize * 1.3,
                    textStyle: {
                        fontSize: titleFontSize / 1.5
                    }
                },
                series: [
                    {
                        barWidth: titleFontSize * 1.2,
                        itemStyle: {
                            barBorderRadius: [this.getRadius(), 0, 0, this.getRadius()]
                        }
                    },
                    {
                        barWidth: titleFontSize * 1.2,
                        itemStyle: {
                            barBorderRadius: [0, this.getRadius(), this.getRadius(), 0]
                        }
                    }
                ]
            }
            this.chartInstance.setOption(adapterOption)
            // 手动调用图表对象的resize 才能产生效果
            this.chartInstance.resize()
        }
    }
}
</script>

<style lang="less">
</style>
