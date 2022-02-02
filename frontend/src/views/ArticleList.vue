<template>
  <div class="container-fluid main-cards">

    <div class="row" v-for="article in articles" :key="article.id">
      <div class="col-12">
        <div class="card">
          <div class="card-header bg-primary">
            <h5 class="card-title mb-0 text-white">{{ article.title }}</h5>
          </div>
          <div class="card-body">
            {{ article.abstract }}
          </div>
          <div class="card-footer d-flex justify-content-end">
            <router-link :to="{ name: 'article-read', params: {slug: article.slug}}">
              <button class="btn btn-primary btn-lg">Ler</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import api from '../services/api.js';

export default {
  name: 'ArticleList',
  data() {
    return {
      articles: []
    }
  },
  mounted() {
    api.get('/article/').then(response => {
      this.articles = response.data;
    })
  }
}
</script>

<style>

</style>