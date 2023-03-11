import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SearchView from '../views/SearchView.vue'
import RegisterView from '../views/RegisterView.vue'
import ForgotPassView from '../views/ForgotPassView.vue'
import ChangePassView from '../views/ChangePassView.vue'
import ActivateView from '../views/ActivateView.vue'
import EditProfileView from '../views/EditProfileView.vue'
import BookDetailView from '../views/BookDetailView.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    redirect: { path: `/category/art_architecture_photography/8/1` }
  },
  {
    path: '/category/:category_slug',
    name: 'view_book_as_category',
    redirect: { path: `/category/art_architecture_photography/8/1` }
  },
  {
    path: '/category/:category_slug/:books_per_page/:page',
    name: 'view_book_as_category',
    component: HomeView
  },
  {
    path: '/category/:category_slug/:book_slug',
    name: 'BookDetailView',
    component: BookDetailView
  },
  {
    path: '/search/:books_per_page/:page',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/register',
    name: 'RegisterView',
    component: RegisterView
  },
  {
    path: '/profile',
    name: 'EditProfileView',
    component: EditProfileView
  },
  {
    path: '/activate/:token',
    name: 'ActivateView',
    component: ActivateView
  },
  {
    path: '/forgot_password',
    name: 'ForgotPassView',
    component: ForgotPassView
  },

  {
    path: '/change_password/:token',
    name: 'ChangePassView',
    component: ChangePassView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
