<template>
  <main-layout>
    <template v-slot:content>
      <div class="container-fluid main-cards main-layout-container">
        <h1 class="h2 mb-3">Criar artigo</h1>

        <div class="row">
          <div class="col-12">

            <form @submit.prevent="createArticle">

              <div class="card">
                <div class="card-header">
                  <h5 class="card-title mb-0">Título</h5>
                </div>
                <div class="card-body pt-0">
                  <input type="text" class="form-control" v-model="title" required>
                </div>
              </div>

              <div class="card">
                <div class="card-header">
                  <h5 class="card-title mb-0">Resumo</h5>
                </div>
                <div class="card-body pt-0">
                  <textarea class="form-control" rows="2" v-model="abstract"></textarea>
                </div>
              </div>

              <div class="card">
                <div class="card-header">
                  <h5 class="card-title mb-0">Artigo</h5>
                </div>
                <div class="card-body pt-0">
                  <TinyMCE
                    v-model="content"
                  />
                </div>
              </div>

              <div class="card">
                <div class="card-body d-flex justify-content-end">
                  <button class="btn btn-primary btn-lg" type="submit">Publicar</button>
                </div>
              </div>

            </form>
          </div>
        </div>
      </div>
    </template>
  </main-layout>
</template>

<script>
import api from "../services/api.js"

import TinyMCE from "../components/TinyMCE.vue"
import MainLayout from "../layouts/MainLayout.vue"

import { getYear, getMonth } from "../services/utils.js"

export default {
  name: 'ArticleCreate',
  components: {
    MainLayout,
    TinyMCE
  },
  data() {
    return {
      title: '',
      abstract: '',
      content: ''
    }
  },
  methods: {
    createArticle() {
      var headers = {'Content-Type': "application/json"}
      var requestBody = {
        title: this.title,
        abstract: this.abstract,
        content: this.content
      }
      api.post('/article/', requestBody, headers).then(response => {
        if (response.data) {
          const year = getYear(response.data.published_at);
          const month = getMonth(response.data.published_at);
          const slug = response.data.slug;

          this.$router.push({ path: `/article/${year}/${month}/${slug}`})
        }
      })
    }
  }
}
</script>

<style>
</style>