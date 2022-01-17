import { createStore } from 'vuex'

import SideBarModule from "./modules/sidebar.js"

const store = new createStore({
  modules: {
    sidebarmodule: SideBarModule
  }
})

export default store;