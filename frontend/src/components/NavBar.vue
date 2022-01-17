<template>
  <nav class="navbar navbar-expand navbar-light navbar-bg">
    <a class="sidebar-toggle js-sidebar-toggle" @click="toggleSidebar">
      <i class="hamburger align-self-center"></i>
    </a>
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="h1 nav-link mb-0" href="/">Leonardo de Paula</a>
      </li>
    </ul>
    <div class="navbar-collapse collapse">
      <ul class="navbar-nav navbar-align">
        <li class="nav-item dropdown">
          <a class="nav-icon dropdown-toggle d-inline-block d-sm-none" href="#" data-bs-toggle="dropdown">
            <i class="align-middle" data-feather="settings"></i>
          </a>

          <a class="nav-link dropdown-toggle d-none d-sm-inline-block" href="#" data-bs-toggle="dropdown">
            <img src="../assets/logo.png" class="avatar img-fluid rounded me-1" alt="Charles Hall" /> <span class="text-dark">Leonardo de Paula</span>
          </a>
          <div class="dropdown-menu dropdown-menu-end">
            <a class="dropdown-item" href="@"><i class="align-middle me-1" data-feather="user"></i> Profile</a>
            <a class="dropdown-item" href="#">Log out</a>
          </div>
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
        type: 'sidebarmodule/toggleSidebar'
      })
		}
	}
}
</script>

<style>

</style>