import { createRouter, createWebHistory } from 'vue-router';

import MainLayout from '../layouts/MainLayout.vue'
import LoginLayout from '../layouts/LoginLayout.vue'

import Artigos from '../views/Artigos.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: MainLayout,
      children: [
        {
          path: '/artigos',
          name: 'artigos-list',
          component: Artigos
        }
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: LoginLayout
    },
  ]
});

export default router;