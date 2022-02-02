<template>
  <div class="container-fluid main-cards">

    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-header bg-primary">
            <h5 class="card-title mb-0 text-white">
              {{ article.title }}
              <span class="float-end">Publicação: {{ articleDate }}</span>
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
import moment from 'moment';

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
      const data = moment.utc(this.article.published_at)
      return data.format("DD/MM/YYYY HH:mm")
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