import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import RegisterUser from '@/views/RegisterUser.vue'
import Tasks from "@/views/Tasks";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/reg',
    name: 'RegisterUser',
    component: RegisterUser
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: Tasks
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
