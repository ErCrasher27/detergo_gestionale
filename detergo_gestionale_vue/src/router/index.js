import { createRouter, createWebHistory } from 'vue-router'
import Acceptance from '../views/Acceptance.vue'

const routes = [
  {
    path: '/acceptance',
    name: 'acceptance',
    component: Acceptance
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
