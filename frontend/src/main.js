import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'  // Import axios

// Configure Axios for CSRF token
axios.defaults.xsrfCookieName = 'csrftoken';  // Set the CSRF cookie name
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"; // Set the CSRF header name

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')