import { createApp } from 'vue';
import App from './App.vue';
import store from './store/index.js';
import router from './services/routes.js';

import "./assets/js/app.js";
import "./assets/css/app.css";

import { library } from '@fortawesome/fontawesome-svg-core';
import { faHome, faNewspaper, faIdCard, faEnvelope, faExclamationCircle, faBook, faBriefcase, faLightbulb, faNetworkWired, faCamera } from '@fortawesome/free-solid-svg-icons';
import { faLinkedin, faGithub, faKaggle } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(faHome, faNewspaper, faIdCard, faEnvelope, faCamera, faExclamationCircle, faBook, faBriefcase, faLightbulb, faNetworkWired, faLinkedin, faGithub, faKaggle);

const app = createApp(App);

app.use(store);
app.use(router);
app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app');
