import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import "./assets/css/style.css"

axios.defaults.baseURL= 'https://lamnv-book-store.herokuapp.com'
axios.defaults.headers.common['Authorization'] = 'jwt' + localStorage.getItem('jwt')

createApp(App).use(store).use(router, axios).mount('#app')
