import api from '../../services/api.js';
import router from '../../services/routes.js'

const AuthenticationModule = {
  namespaced: true,
  state: {
    token: null,
    user: null,
    loggedStatus: false,
    logginError: null
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
    },
    setLoginError(state, payload) {
      state.logginError = payload.loginError
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

        context.commit('setLoginError', {loginError: null})

        if (response.data.access_token) {
          context.commit('setLogin', {token: response.data.access_token, user: response.data.user})
          api.defaults.headers.common = {'Authorization': `Bearer ${response.data.access_token}`}
        }

        if (router.currentRoute.value.query.next) {
          router.push(router.currentRoute.value.query.next);
        } else {
          router.go(-1)
        }

      })
      .catch((error) => {
        context.commit('setLoginError', {loginError: error.response.data.detail})
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
    },
    getLoginError(state) {
      return state.logginError;
    }
  }
}

export default AuthenticationModule;