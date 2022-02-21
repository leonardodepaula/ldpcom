<template>
  <main-layout>
    <template v-slot:content>
      <div class="container-fluid main-cards main-layout-container">
        <h1 class="h2 mb-3">Encaminhar mensagem de contato</h1>

        <div class="row">
          <div class="col-12">

            <form @submit.prevent="createContact">

              <div class="d-flex justify-content-center" v-if="successMessage">
                <div class="col-6">
                  <div class="mb-3" v-if="true">
                    <div class="alert alert-success h4 text-center" role="alert">
                      {{ successMessage }}
                    </div>
                  </div>
                </div>
              </div>

              <div class="d-flex justify-content-center" v-if="errorMessage">
                <div class="col-6">
                  <div class="mb-3" v-if="true">
                    <div class="alert alert-danger h4 text-center" role="alert">
                      {{ errorMessage }}
                    </div>
                  </div>
                </div>
              </div>

              <div class="card">
                <div class="card-header">
                  <h5 class="card-title mb-0">Email</h5>
                </div>
                <div class="card-body pt-0">
                  <input type="email" class="form-control" v-model="email" required>
                </div>
              </div>

              <div class="card">
                <div class="card-header">
                  <h5 class="card-title mb-0">Assunto</h5>
                </div>
                <div class="card-body pt-0">
                  <textarea class="form-control" rows="1" v-model="subject"></textarea>
                </div>
              </div>

              <div class="card">
                <div class="card-header">
                  <h5 class="card-title mb-0">Mensagem</h5>
                </div>
                <div class="card-body pt-0">
                  <TinyMCE
                    v-model="content"
                  />
                </div>
              </div>

              <div class="card">
                <div class="card-body d-flex justify-content-end">
                  <button class="btn btn-primary btn-lg" type="submit">Encaminhar</button>
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

export default {
  name: 'ContactCreate',
  components: {
    MainLayout,
    TinyMCE
  },
  data() {
    return {
      email: '',
      subject: '',
      content: '',
      successMessage: '',
      errorMessage: ''
    }
  },
  methods: {
    createContact() {
      var headers = {'Content-Type': "application/json"}
      var requestBody = {
        email: this.email,
        subject: this.subject,
        content: this.content
      }
      api.post('/contact/', requestBody, headers)
      .then(response => {
        if (response.data) {
          this.successMessage = 'Mensagem encaminhada com sucesso.'
          this.email = ''
          this.subject  = ''
          this.content = ''
          window.scrollTo(0,0);
        }
      })
      .catch((error) => {
        this.errorMessage = error.response.data.detail
        window.scrollTo(0,0);
      })
    }
  }
}
</script>

<style>
</style>