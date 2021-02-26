import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import RegisterUser from '@/views/RegisterUser.vue'
import LoginUser from '@/views/LoginUser.vue'
import Tasks from "@/views/Tasks";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sign_up',
    name: 'RegisterUser',
    component: RegisterUser
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: Tasks
  },
  {
    path: '/log_in',
    name: 'Tasks',
    component: LoginUser
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
