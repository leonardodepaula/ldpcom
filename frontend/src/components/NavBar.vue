<template>
  <nav class="navbar navbar-expand navbar-light navbar-bg">
    <a class="sidebar-toggle js-sidebar-toggle" @click="toggleSidebar">
      <i class="hamburger align-self-center"></i>
    </a>
    <ul class="navbar-nav">
      <li class="nav-item">
        <router-link class="h1 navbar-text mb-0" :to="{name: 'home'}">Leonardo de Paula</router-link>
      </li>
    </ul>
    <div class="navbar-collapse collapse">
      <ul class="navbar-nav navbar-align">
        <li class="nav-item dropdown">
          <a class="nav-icon dropdown-toggle d-inline-block d-sm-none" href="#" data-bs-toggle="dropdown">
            <i class="align-middle" data-feather="settings"></i>
          </a>

          <div v-if="user">
            <a class="nav-link d-none d-sm-inline-block navbar-text" href="#" data-bs-toggle="dropdown">
              <span class="h4 navbar-text me-2">{{ user.full_name }}</span>
              <span class="dropdown-toggle navbar-text"></span>
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
      });
      if (this.$route.meta.requiresAuth) {
        const loginpath = window.location.pathname;
        this.$router.push({name: 'login', query: {next: loginpath}})
      }
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

<style scoped>

.navbar-text {
  color: #495057;
  text-decoration: none;
}
 .navbar {
   height: 80px;
 }

</style>