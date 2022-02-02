<template>
  <main-layout>
    <template v-slot:content>
      <div class="container d-flex flex-column">
        <div class="row">
          <div class="col-6 mx-auto d-table">
            <div class="d-table-cell align-middle">
              <div class="card">
                <div class="card-body mt-5 mb-5">
                  <div class="text-center">
                    <font-awesome-icon icon="exclamation-circle" size="6x"/>
                    <p class="align-middle font-alert mt-2 mb-1">Erro <b>404</b></p>
                    <p class="h3 mt-0">
                      Página não encontrada.
                    </p>
                    <button class="btn btn-primary btn-lg mt-4" @click="goBack">Voltar</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
  </main-layout>
</template>

<script>
import MainLayout from "../layouts/MainLayout.vue"

export default {
  name: 'PageNotFound',
  components: {
    MainLayout
  },
  methods: {
    goBack() {
      this.$router.go(-1)
    }
  }
}
</script>

<style>

.font-alert {
  font-size: 60px;
}

</style>