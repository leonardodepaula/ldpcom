<template>
  <main-layout>
    <template v-slot:content>
      <ErrorCard
        :errorCode="this.error.status"
        :errorMessage="this.error.data.detail"
        v-if="error"
      />
      <div class="container-fluid main-cards" v-else>
        <div class="row">
          <div class="col-12">
            <div class="card border">
              <div class="card-header bg-primary">
                <h5 class="card-title mb-0 text-white text-justify">
                  {{ article.title }}
                </h5>
              </div>
              <div class="card-body border-bottom">
                <span class="mb-0 text-justify" v-html="article.content"></span>
              </div>
              <div class="card-footer bg-light">
                <span class="float-start"><b>Publicação: {{ articleDate }}</b></span>
                <button class="btn btn-primary float-end" @click="goBack">Voltar</button>
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
import ErrorCard from '../components/ErrorCard.vue'

import MainLayout from "../layouts/MainLayout.vue"

export default {
  name: 'ArticleRead',
  components: {
    MainLayout,
    ErrorCard
  },
  data() {
    return {
      article: {
        title: '',
        author: '',
        content: ''
      },
      error: null
    }
  },
  computed: {
    articleDate() {
      const data = moment.utc(this.article.published_at)
      return data.tz('America/Sao_Paulo').format("DD/MM/YYYY HH:mm")
    }
  },
  beforeMount() {
    const year = this.$route.params.year;
    const month = this.$route.params.month;
    const slug = this.$route.params.slug;

    api.get(`/article/${year}/${month}/${slug}`).then(response => {
      this.article = response.data;
    })
    .catch((error) => {
      this.error = error.response;
    })
  },
  methods: {
    goBack() {
      this.$router.go(-1)
    }
  }
}
</script>

<style>

</style>