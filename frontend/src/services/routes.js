import { createRouter, createWebHistory } from 'vue-router';

import MainView from '../views/MainView.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: MainView
    },
    {
      path: '/login',
      component: LoginView
    },
  ]
});

export default router;