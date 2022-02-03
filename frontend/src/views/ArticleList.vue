<template>
  <main-layout>
    <template v-slot:content>
      <div class="container-fluid main-cards">

        <div class="row" v-if="loggedStatus">
          <router-link :to="{ name: 'article-create'}">
            <button class="btn btn-primary mb-3">Criar artigo</button>
          </router-link>
        </div>

        <div class="row" v-for="article in articles" :key="article.id">
          <div class="col-12">
            <div class="card border">
              <div class="card-header bg-primary">
                <h5 class="card-title mb-0 text-white text-justify">{{ article.title }}</h5>
              </div>
              <div class="card-body text-justify">
                {{ article.abstract }}
              </div>
              <div class="card-footer">
                <span class="float-start">Publicação: {{ formatDate(article.published_at) }}</span>
                <router-link :to="{ name: 'article-read', params: {year: getYear(article.published_at), month: getMonth(article.published_at), slug: article.slug}}">
                  <button class="btn btn-primary float-end">Ler</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>

      </div>
    </template>
  </main-layout>
</template>

<script>
import api from '../services/api.js';
import moment from 'moment-timezone';
import MainLayout from "../layouts/MainLayout.vue"

export default {
  name: 'ArticleList',
  components: {
    MainLayout
  },
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
    },
    getYear(date) {
      const dateForConversion = moment.utc(date)
      return dateForConversion.tz('America/Sao_Paulo').format("YYYY")
    },
    getMonth(date) {
      const dateForConversion = moment.utc(date)
      return dateForConversion.tz('America/Sao_Paulo').format("MM")
    }
  },
  computed: {
    loggedStatus() {
      return this.$store.state.authentication.loggedStatus
    }
  }
}
</script>

<style>

</style>