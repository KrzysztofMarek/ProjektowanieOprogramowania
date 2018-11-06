import '@babel/polyfill'
import Vue from 'vue'
import './plugins/vuetify'
import VueRouter from 'vue-router'

import { store } from "./store"
import App from './App.vue'
import Order from "./components/Order" 
import Browse from "./components/Browse" 

Vue.config.productionTip = false

Vue.use(VueRouter);

const routes = [
  { path: "/checkout",  component: Order },
  { path: "/browse",  component: Browse }
];

const router = new VueRouter({ routes, mode: 'history' });

new Vue({
  render: h => h(App),
  router,
  store,
}).$mount('#app')
