<template>
  <div class="container-fluid main-cards">
    <h1 class="h3 mb-3">Criar artigo</h1>

    <div class="row">
      <TinyMCE />
    </div>
  </div>
</template>

<script>
import TinyMCE from "../components/TinyMCE.vue"

export default {
  name: 'CreateArticle',
  components: {
    TinyMCE
  },
}
</script>

<style>
</style>