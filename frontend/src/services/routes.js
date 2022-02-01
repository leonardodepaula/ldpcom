import { createRouter, createWebHistory } from 'vue-router';

import MainLayout from '../layouts/MainLayout.vue'
import LoginLayout from '../layouts/LoginLayout.vue'

import ArticleList from '../views/ArticleList.vue'
import ArticleCreate from '../views/ArticleCreate.vue'

import store from '../store/index.js'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: MainLayout,
      children: [
        {
          path: '/article',
          name: 'article-list',
          component: ArticleList
        },
        {
          path: '/article/create',
          name: 'article-create',
          component: ArticleCreate,
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

router.beforeEach((to, from, next) => {

  const loginpath = window.location.pathname;
  const loggedStatus = store.state.authentication.loggedStatus
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)

  if (!loggedStatus && requiresAuth && loginpath != '/login') {
    next({ name: 'login', query: {next: loginpath} });
  } else {
    next();
  }
})

export default router;