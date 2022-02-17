import { createRouter, createWebHistory } from 'vue-router';
import multiguard from 'vue-router-multiguard';

import LoginLayout from '../layouts/LoginLayout.vue'
import ArticleList from '../views/ArticleList.vue'
import ArticleCreate from '../views/ArticleCreate.vue'
import ArticleRead from '../views/ArticleRead.vue'
import PageNotFound from '../views/PageNotFound.vue'
import Biography from '../views/Biography.vue'
import HomePage from '../views/HomePage.vue'

import { loggingMiddleware, requireAuthMiddleware } from './middleware.js';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage,
      beforeEnter: multiguard([loggingMiddleware])
    },
    {
      path: '/login',
      name: 'login',
      component: LoginLayout,
      beforeEnter: multiguard([loggingMiddleware])
    },
    {
      path: '/article',
      name: 'article-list',
      component: ArticleList,
      beforeEnter: multiguard([loggingMiddleware])
    },
    {
      path: '/article/create',
      name: 'article-create',
      component: ArticleCreate,
      beforeEnter: multiguard([loggingMiddleware, requireAuthMiddleware]),
    },
    {
      path: '/article/:year/:month/:slug',
      name: 'article-read',
      component: ArticleRead,
      beforeEnter: multiguard([loggingMiddleware])
    },
    {
      path: '/biography',
      name: 'biography',
      component: Biography,
      beforeEnter: multiguard([loggingMiddleware])
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'page-not-found',
      component: PageNotFound,
      beforeEnter: multiguard([loggingMiddleware])
    },
  ]
});

export default router;