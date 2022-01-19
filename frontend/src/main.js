import { createApp } from 'vue'
import App from './App.vue'
import store from './store/index.js'
import router from './services/routes.js'

import "./assets/js/app.js"
import "./assets/css/app.css"

const app = createApp(App);

app.use(store);
app.use(router);

app.mount('#app');
