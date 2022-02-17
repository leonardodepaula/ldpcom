import store from '../store/index.js'

const loggingMiddleware = function(to, from, next) {
  console.log(to.params, to.query, to.fullPath)
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