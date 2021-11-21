import Vue from 'vue';

// vue-router
import VueRouter from 'vue-router';
Vue.use(VueRouter);

// axios
import axios from 'axios';
axios.defaults.baseURL = 'http://localhost:8080';
// axios.defaults.baseURL = 'http://10.254.66.150:8080';
Vue.prototype.$http = axios;

// element-ui
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

// video
import VideoPlayer from 'vue-video-player';
import 'vue-video-player/src/custom-theme.css';
import 'video.js/dist/video-js.css';
Vue.use(VideoPlayer);

// echarts
import * as echarts from 'echarts'
Vue.prototype.$echarts = echarts;

// assets
import './assets/font/iconfont.css'
import './assets/css/global.less'

// dayjs
import dayjs from 'dayjs'
import utc from 'dayjs/plugin/utc'
dayjs.extend(utc);
Vue.prototype.$dayjs = dayjs;

// tools
import tools from '@/tools'
Vue.prototype.$tools = tools

// WebSocket
import SocketService from '@/utils/socket_service'
SocketService.Instance.connect()
Vue.prototype.$socket = SocketService.Instance

// tip
Vue.config.productionTip = false;

// main
import App from './App.vue';
import router from './router';

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
