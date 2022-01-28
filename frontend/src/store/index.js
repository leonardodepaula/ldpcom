import { createStore } from 'vuex'
import createPersistedState from "vuex-persistedstate";

import SideBarModule from "./modules/sidebar.js"
import AuthenticationModule from './modules/authentication.js';

const store = new createStore({
  modules: {
    sidebar: SideBarModule,
    authentication: AuthenticationModule
  },
  plugins: [createPersistedState()]
})

export default store;