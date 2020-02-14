import Vue from 'vue'
import Router from 'vue-router'
import SearchGps from '@/components/SearchGps'
import GpsCanvas from '@/components/GpsCanvas'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SearchGps',
      component: SearchGps
    },
    {
      path: '/GpsCanvas',
      name: 'GpsCanvas',
      component: GpsCanvas
    }
  ]
})
