import axios from 'axios';
import store from '../store/index.js'
import router from '../services/routes.js'

const api = axios.create({
  baseURL: `http://${process.env.VUE_APP_API_HOST}:8000/`,
})

// Headers
api.defaults.headers.common = {'Access-Control-Allow-Origin': '*'}

// Nas chamadas da API, verifica se houve erro relativo à autorização/autenticação
// e encaminha o usuário para a página de login.
api.interceptors.response.use(function (response) {
  return response;
  }, function (error) {
  const anauthorizedErrors = [401, 403]
  if (anauthorizedErrors.includes(error.response.status)) {
    store.dispatch({
      type: 'authentication/logout'
    });
    const loginpath = window.location.pathname;
    router.push({name: 'login', query: {next: loginpath}})
  } else {
    throw error;
  }
  });

export default api;