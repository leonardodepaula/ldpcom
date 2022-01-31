import { createRouter, createWebHistory } from 'vue-router';

import MainLayout from '../layouts/MainLayout.vue'
import LoginLayout from '../layouts/LoginLayout.vue'

import Artigos from '../views/Artigos.vue'
import CreateArticle from '../views/CreateArticle.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: MainLayout,
      children: [
        {
          path: '/articles',
          name: 'artigos-list',
          component: Artigos
        },
        {
          path: '/create-article',
          name: 'artigos-create',
          component: CreateArticle
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