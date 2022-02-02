<template>
  <main-layout>
    <template v-slot:content>
      <div class="container-fluid main-cards">
        <div class="row">
          <div class="col-12">
            <div class="card">
              <div class="card-header bg-primary">
                <h5 class="card-title mb-0 text-white text-justify">
                  {{ article.title }}
                </h5>
              </div>
              <div class="card-body">
                <span class="mb-0 text-justify" v-html="article.content"></span>
              </div>
              <div class="card-footer bg-light">
                <span class="float-start">Publicação: {{ articleDate }}</span>
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
  name: 'ArticleRead',
  components: {
    MainLayout,
  },
  data() {
    return {
      article: {
        title: '',
        author: '',
        content: ''
      }
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
  }
}
</script>

<style>

</style>