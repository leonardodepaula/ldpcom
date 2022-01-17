import { createStore } from 'vuex'
import createPersistedState from "vuex-persistedstate";

import SideBarModule from "./modules/sidebar.js"

const store = new createStore({
  modules: {
    sidebarmodule: SideBarModule
  },
  plugins: [createPersistedState()]
})

export default store;