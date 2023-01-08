import { createRouter, createWebHistory } from 'vue-router'
import Accettazione from '../views/Accettazione.vue'

const routes = [
  {
    path: '/accettazione',
    name: 'accettazione',
    component: Accettazione
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
