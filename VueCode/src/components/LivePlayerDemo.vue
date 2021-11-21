<template>
<div class="hello">

    <!-- <div style="width:512px;height:300px;margin:auto">
        <LivePlayer videoUrl="video.mp4" />
    </div> -->
    <div style="width:512px;height:300px;margin:auto">
        <LivePlayer  @snapOutside="snapOutside" ref="player2" videoUrl="http://localhost:8999/video.flv" live />
    </div>
</div>
</template>

<script>
import LivePlayer from '@liveqing/liveplayer'
export default {
    name: 'LivePlayerDemo',
    components: {
        LivePlayer
    },
    props: {
        msg: String
    },
    methods: {
        pause: function () {
            this.$refs.player2.pause();
        },
        play: function () {
            this.$refs.player2.play();
        },
        snap: function () {
            this.$refs.player2.snap();
        },
        snapOutside: function (snapData) {
            alert(snapData)
        }
    }
}
</script>
