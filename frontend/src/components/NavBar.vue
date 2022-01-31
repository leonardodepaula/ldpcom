<template>
  <nav class="navbar navbar-expand navbar-light navbar-bg">
    <a class="sidebar-toggle js-sidebar-toggle" @click="toggleSidebar">
      <i class="hamburger align-self-center"></i>
    </a>
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="h1 nav-link mb-0">Leonardo de Paula</a>
      </li>
    </ul>
    <div class="navbar-collapse collapse">
      <ul class="navbar-nav navbar-align">
        <li class="nav-item dropdown">
          <a class="nav-icon dropdown-toggle d-inline-block d-sm-none" href="#" data-bs-toggle="dropdown">
            <i class="align-middle" data-feather="settings"></i>
          </a>

          <div v-if="user">
            <a class="nav-link d-none d-sm-inline-block" href="#" data-bs-toggle="dropdown">
              <span class="h4 text-dark me-2">{{ user.full_name }}</span>
              <span class="dropdown-toggle"></span>
            </a>
            <div class="dropdown-menu dropdown-menu-end">
              <a class="dropdown-item" @click="logout">Log out</a>
            </div>
          </div>
          <router-link :to="{ name: 'login' }" v-else>
            <button class="btn btn-primary">Login</button>
          </router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  methods: {
		toggleSidebar() {
			this.$store.dispatch({
        type: 'sidebar/toggleSidebar'
      })
		},
    logout() {
			this.$store.dispatch({
        type: 'authentication/logout'
      })
		},
	},
  computed: {
    loggedStatus() {
      return this.$store.state.authentication.loggedStatus
    },
    user() {
      return this.$store.state.authentication.user
    }
  }
}
</script>

<style>

</style>