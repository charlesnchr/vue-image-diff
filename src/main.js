import Vue from 'vue'
import App from './App'
// import App2 from './App2'

/*
import VueLodash from 'vue-lodash'
import cornerstonePlugin from '@/plugins/cornerstonePlugin'
import mModal from '@/plugins/modal'

Vue.use(VueLodash)
Vue.use(cornerstonePlugin)
Vue.use(mModal)
*/

new Vue({
  render: h => h(App),
  components: { App }
}).$mount('#app')

//
//
// new Vue({
//     components: { App },
//     el: '#app'
// })
//

// new Vue({
//   render: h => h(App2),
//   components: { App2 }
// }).$mount('#app')
