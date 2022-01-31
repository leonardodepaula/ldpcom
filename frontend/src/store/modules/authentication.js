import api from '../../services/api.js';
import router from '../../services/routes.js';

const AuthenticationModule = {
  namespaced: true,
  state: {
    token: null,
    user: null,
    loggedStatus: false,
  },
  mutations: {
    setLogin(state, payload) {
      state.token = payload.token;
      state.user = payload.user;
      state.loggedStatus = true;
    },
    setLogout(state) {
      state.token = null;
      state.user = null;
      state.loggedStatus = false;
    }
  },
  actions: {
    login(context, payload) {
      var bodyFormData = new FormData()
      bodyFormData.append('username', payload.email)
      bodyFormData.append('password', payload.password)

      var headers = {'Content-Type': "application/x-www-form-urlencoded"}
      
      api.post('auth/login', bodyFormData, headers)
      .then(response => {
        if (response.data.access_token) {
          context.commit('setLogin', {token: response.data.access_token, user: response.data.user})
          api.defaults.headers.common = {'Authorization': `Bearer ${response.data.access_token}`}
          router.push({name: 'home'})
        }
      })
      .catch((error) => {
        console.log(error.response.data.detail)
      })
    },
    logout(context) {
      context.commit('setLogout');
    }
  },
  getters: {
    getUser(state) {
      return state.user;
    },
    getLoggedState(state) {
      return state.userIsLoggedIn;
    }
  }
}

export default AuthenticationModule;