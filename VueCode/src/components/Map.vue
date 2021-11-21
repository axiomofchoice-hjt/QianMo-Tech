<template>
  <div class='com-container'>
        <div class='com-chart' ref='map_ref'></div>
    </div>
</template>

<script>
import '../../public/static/bmap/bmap'
export default {
    data () {
        return {
            chartInstance: null,
            allData: null,
            points: null, // 所有的坐标
            getTimerID: null
        }
    },
    created () {
        this.$socket.registerCallBack('mapData', this.getData)
    },
    mounted () {
        // this.getData()
        this.$socket.send({
            action: 'getData',
            socketType: 'mapData',
            chartName: 'map',
            value: ''
        })
        this.getTimerID = setInterval(() => {
            setTimeout(
                this.$socket.send({
                    action: 'getData',
                    socketType: 'mapData',
                    chartName: 'map',
                    value: ''
                }), 0)
        }, 60000)
    },
    methods: {
        getData (ret) {
                this.allData = ret
                this.points = [].concat.apply([], this.allData.map(function (track) {
                    return track.map(function (seg) {
                        return seg.coord.concat([1])
                    })
                }))
                // console.log(this.points)
            this.DrawHeatMap ()
        },

        DrawHeatMap () {
            this.chartInstance = this.$echarts.init(this.$refs.map_ref)
            const option = {
                animation: false,
                bmap: {
                    center: [120.13066322374, 30.240018034923],
                    zoom: 14,
                    roam: true
                },
                visualMap: {
                    show: false,
                    top: 'top',
                    min: 0,
                    max: 5,
                    seriesIndex: 0,
                    calculable: true,
                    inRange: {
                        color: ['blue', 'blue', 'green', 'yellow', 'red']
                    }
                },
                series: [{
                    type: 'heatmap',
                    coordinateSystem: 'bmap',
                    data: this.points,
                    pointSize: 5,
                    blurSize: 6
                }]
            }
            this.chartInstance.setOption(option)
            console.log(this.chartInstance)
            // 添加百度地图插件
            this.chartInstance.getModel().getComponent('bmap').getBMap()
        },
        screenAdapter () {
          this.chartInstance = this.$echarts.init(this.$refs.map_ref)
            const option = {
                animation: false,
                bmap: {
                    center: [120.13066322374, 30.240018034923],
                    zoom: 14,
                    roam: true
                },
                visualMap: {
                    show: false,
                    top: 'top',
                    min: 0,
                    max: 5,
                    seriesIndex: 0,
                    calculable: true,
                    inRange: {
                        color: ['blue', 'blue', 'green', 'yellow', 'red']
                    }
                },
                series: [{
                    type: 'heatmap',
                    coordinateSystem: 'bmap',
                    data: this.points,
                    pointSize: 5,
                    blurSize: 6
                }]
            }
            this.chartInstance.setOption(option)
            console.log(this.chartInstance)
            // 添加百度地图插件
            this.chartInstance.getModel().getComponent('bmap').getBMap()
        }
        
    },
    destroyed () {
        this.$socket.unRegisterCallBack('mapData')
        clearInterval(this.getTimerID)
    }
}
</script>

<style lang="less" scoped>

</style>
