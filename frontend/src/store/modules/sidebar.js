const SideBarModule = {
  namespaced: true,
  state: {
    sidebarIsCollapsed: false
  },
  mutations: {
    toggleSidebar(state) {
      state.sidebarIsCollapsed = !state.sidebarIsCollapsed
    }
  },
  actions: {
    toggleSidebar(context) {
      context.commit('toggleSidebar')
    }
  },
  getters: {
    getSidebarStatus(state) {
      return state.sidebarIsCollapsed
    }
  }
}

export default SideBarModule;