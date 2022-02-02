<template>
  <div class="container-fluid main-cards">

    <div class="row" v-for="article in articles" :key="article.id">
      <div class="col-12">
        <div class="card">
          <div class="card-header bg-primary">
            <h5 class="card-title mb-0 text-white text-justify">{{ article.title }}</h5>
          </div>
          <div class="card-body text-justify">
            {{ article.abstract }}
          </div>
          <div class="card-footer">
            <span class="float-start">Publicação: {{ formatDate(article.published_at) }}</span>
            <router-link :to="{ name: 'article-read', params: {slug: article.slug}}">
              <button class="btn btn-primary btn-lg float-end">Ler</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import api from '../services/api.js';
import moment from 'moment-timezone';

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
  },
  methods: {
    formatDate(date) {
      const dateForConversion = moment.utc(date)
      return dateForConversion.tz('America/Sao_Paulo').format("DD/MM/YYYY HH:mm")
    }
  }
}
</script>

<style>

</style>