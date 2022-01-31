<template>
  <nav
    id="sidebar"
    class="sidebar js-sidebar"
    :class="{collapsed: sidebarCollapsed}"
  >
    <div class="sidebar-content js-simplebar">
      <ul class="sidebar-nav mt-3">

        <li class="sidebar-item">
          <router-link class="sidebar-link" to="/">
            <i class="align-middle" data-feather="home"></i> <span class="align-middle">Homepage</span>
          </router-link>
        </li>

        <li class="sidebar-item">
          <router-link class="sidebar-link" to="/artigos">
            <i class="align-middle" data-feather="book"></i> <span class="align-middle">Artigos</span>
          </router-link>
        </li>

        <li class="sidebar-item">
          <a class="sidebar-link" href="#">
            <i class="align-middle" data-feather="user"></i> <span class="align-middle">Biografia</span>
          </a>
        </li>

        <li class="sidebar-item">
          <a class="sidebar-link" href="#">
            <i class="align-middle" data-feather="mail"></i> <span class="align-middle">Contato</span>
          </a>
        </li>

      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  computed: {
    sidebarCollapsed() {
      return this.$store.getters['sidebar/getSidebarStatus']
    }
  }
}
</script>

<style>

</style>