import VueRouter from 'vue-router';
import Home from '@/views/Home.vue';
import UserInfo from '@/components/UserInfo.vue';
import UserMessage from '@/components/UserMessage.vue';
import UserVehicle from '@/components/UserVehicle.vue';
import UserRecord from '@/components/UserRecord.vue';
import UserChangeInfo from '@/components/UserChangeInfo.vue';
import AdminHome from '@/components/AdminHome.vue';
import AdminRecord from '@/components/AdminRecord.vue';
import AdminNewRecord from '@/components/AdminNewRecord.vue';
import AdminCheckRecord from '@/components/AdminCheckRecord.vue';
import AdminCamera from '@/components/AdminCamera.vue';
import ScreenPage from '@/views/ScreenPage.vue';
import UserPage from '@/views/UserPage';
import AdminPage from '@/views/AdminPage';

const originalPush = VueRouter.prototype.push;

VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err);
};

export default new VueRouter({
  routes: [
    { path: "/", component: Home, },
    {
      path: "/user", component: UserPage,
      children: [
        { path: "info", component: UserInfo, },
        { path: "info/change", component: UserChangeInfo, },
        { path: "message", component: UserMessage, },
        { path: "vehicle", component: UserVehicle, },
        { path: "record", component: UserRecord, },
      ]
    },
    { path: "/admin/screen", component: ScreenPage },
    {
      path: "/admin", component: AdminPage,
      children: [
        // { path: "home", component: AdminHome },
        { path: "home", redirect: "record" },
        { path: "record", component: AdminRecord },
        { path: "record/:state/:illegal/:partition/:pageindex", component: AdminRecord },
        { path: "record/:date1/:date2/:state/:illegal/:partition/:pageindex", component: AdminRecord },
        { path: "record-new", component: AdminNewRecord },
        { path: "record-check/:serial", component: AdminCheckRecord },
        { path: "camera", component: AdminCamera },
        { path: "camera/:partition/:pageindex/:cameraId", component: AdminCamera },
        { path: "record-edit/:serial", component: AdminNewRecord },
      ]
    },
  ],
});