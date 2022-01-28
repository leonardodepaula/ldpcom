import api from './api.js';

login(user) {
  return api
  .post('auth/get-access-token/', {grant_type: '', username: user.username, password: user.password, scope: '', client_id: '', client_secret: ''})
  .then(response => {
    if (response.data.access_token) {
      localStorage.setItem('user', JSON.stringify(response.data))
    }
  })
};

logout() {
  localStorage.removeItem('user');
};