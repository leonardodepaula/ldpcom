import api from '../../services/api.js'

const AuthenticationModule = {
  namespaced: true,
  state: {
    token: '',
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
    },
  },
  actions: {
    login(context, payload) {
      var bodyFormData = new FormData()
      bodyFormData.append('username', payload.email)
      bodyFormData.append('password', payload.password)

      var headers = {'Content-Type': "application/x-www-form-urlencoded"}
      
      api.post('auth/get-access-token', bodyFormData, headers)
      .then(response => {
        if (response.data.access_token) {
          context.commit('setToken', {token: response.data.access_token})
        }
      })
      .catch((error) => { // eslint-disable-line no-unused-vars
        context.commit('changeError')
      })

    }
  },
  getters: {
  }
}

export default AuthenticationModule;