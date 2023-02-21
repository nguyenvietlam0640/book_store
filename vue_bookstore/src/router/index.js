import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SearchView from '../views/SearchView.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    redirect: {path: `/category/art_architecture_photography/8/1`}
  },
  {
    path: '/category/:category_slug/:books_per_page/:page',
    name: 'view_book_as_category',
    component: HomeView
  },
  {
    path: '/search/:books_per_page/:page',
    name: 'SearchView',
    component: SearchView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
