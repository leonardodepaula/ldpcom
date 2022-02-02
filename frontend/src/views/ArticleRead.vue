<template>
  <div class="container-fluid main-cards">

    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-header bg-primary">
            <h5 class="card-title mb-0 text-white">
              {{ article.title }}
              <span class="float-end">Data de publicação: {{ articleDate }}</span>
            </h5>
          </div>
          <div class="card-body">
            <span class="mb-0" v-html="article.content"></span>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import api from '../services/api.js';

export default {
  name: 'ArticleRead',
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
      return this.article.published_at
    }
  },
  beforeMount() {
    api.get(`/article/${this.$route.params.slug}`).then(response => {
      this.article = response.data;
    })
  }
}
</script>

<style>

</style>