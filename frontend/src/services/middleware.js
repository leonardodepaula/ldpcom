import store from '../store/index.js'
import api from './api.js'

const loggingMiddleware = function(to, from, next) {
  var headers = {'Content-Type': "application/json"}
  var requestBody = {
    path: to.fullPath,
    params: to.params,
    query: to.query
  }
  api.post('/log/', requestBody, headers)
  next();
}

const requireAuthMiddleware = function(to, from, next) {

  const loginpath = window.location.pathname;
  const loggedStatus = store.state.authentication.loggedStatus

  if (!loggedStatus && loginpath != '/login') {
    next({ name: 'login', query: {next: loginpath} });
  } else {
    next();
  }
}

export { loggingMiddleware, requireAuthMiddleware }