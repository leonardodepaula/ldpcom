<template>
  <nav
    id="sidebar"
    class="sidebar js-sidebar"
    :class="{collapsed: sidebarCollapsed}"
  >
    <div class="sidebar-content js-simplebar">
      <ul class="sidebar-nav mt-3">

        <li class="sidebar-item" :class="{active: homepageActive}">
          <router-link class="sidebar-link" :to="{name: 'home'}">
            <font-awesome-icon icon="home" /> <span class="align-middle">Homepage</span>
          </router-link>
        </li>

        <li class="sidebar-item" :class="{active: articleActive}">
          <router-link class="sidebar-link" :to="{name: 'article-list'}">
            <font-awesome-icon icon="newspaper" /> <span class="align-middle">Artigos</span>
          </router-link>
        </li>

        <li class="sidebar-item" :class="{active: biographyActive}">
          <router-link class="sidebar-link" :to="{name: 'biography'}">
            <font-awesome-icon icon="id-card" /> <span class="align-middle">Biografia</span>
          </router-link>
        </li>

        <li class="sidebar-item">
          <a class="sidebar-link" href="#">
            <font-awesome-icon icon="camera" /> <span class="align-middle">Fotografias</span>
          </a>
        </li>

        <li class="sidebar-item">
          <a class="sidebar-link" href="#">
            <font-awesome-icon icon="envelope" /> <span class="align-middle">Contato</span>
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
    },
    homepageActive() {
      if (this.$route.name === 'home') {
        return true
      } else {
        return false
      }
    },
    articleActive() {
      const articleRoutes = ['article-list', 'article-read', 'article-create']
      if (articleRoutes.includes(this.$route.name)) {
        return true
      } else {
        return false
      }
    },
    biographyActive() {
      if (this.$route.name === 'biography') {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style>

</style>