import { createRouter, createWebHistory } from 'vue-router';

import LoginLayout from '../layouts/LoginLayout.vue'

import ArticleList from '../views/ArticleList.vue'
import ArticleCreate from '../views/ArticleCreate.vue'
import ArticleRead from '../views/ArticleRead.vue'
import PageNotFound from '../views/PageNotFound.vue'
import Biography from '../views/Biography.vue'
import FrontPage from '../views/FrontPage.vue'

import store from '../store/index.js'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: FrontPage,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginLayout
    },
    {
      path: '/article',
      name: 'article-list',
      component: ArticleList
    },
    {
      path: '/article/create',
      name: 'article-create',
      component: ArticleCreate,
      meta: { requiresAuth: true }
    },
    {
      path: '/article/:year/:month/:slug',
      name: 'article-read',
      component: ArticleRead,
    },
    {
      path: '/biography',
      name: 'biography',
      component: Biography,
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'page-not-found',
      component: PageNotFound
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