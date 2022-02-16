<template>
  <main-layout>
    <template v-slot:content>
      <main class="flex-shrink-0">
            <!-- Header-->
            <header class="py-5 bg-primary bg-gradient">
                <div class="container px-5">
                    <div class="row gx-5 align-items-center justify-content-center">
                        <div class="col-lg-8 col-xl-7 col-xxl-6">
                            <div class="my-5 text-center text-xl-start">
                                <h1 class="display-5 fw-bolder text-white mb-2">Bem-vindo!</h1>
                                <p class="lead fw-normal text-white-50 mb-4 text-justify">O objetivo desta página é servir de laboratório para testes de desenvolvimento web e machine learning com Python, mas também divulgar artigos e fotografias.</p>
                            </div>
                        </div>
                        <div class="col-xl-5 col-xxl-6 d-none d-xl-block text-center"><img class="img-fluid rounded-3 my-5" src="https://dummyimage.com/600x400/343a40/6c757d" alt="..." /></div>
                    </div>
                </div>
            </header>
            <!-- Blog preview section-->
            <section class="py-5">
              <div class="container">
                <div class="row gx-5">
                  <div class="col-lg-4">
                    <div class="card h-100 shadow border-0">
                      <img class="card-img-top" src="https://dummyimage.com/600x350/ced4da/6c757d" alt="..." />
                      <div class="card-body p-4">
                        <div class="badge bg-primary bg-gradient rounded-pill mb-2">News</div>
                        <a class="text-decoration-none link-dark stretched-link" href="#!"><h5 class="card-title mb-3">Blog post title</h5></a>
                        <p class="card-text mb-0">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                      </div>
                        <div class="card-footer p-4 pt-0 bg-transparent border-top-0">
                          <div class="d-flex align-items-end justify-content-between">
                            <div class="d-flex align-items-center">
                              <img class="rounded-circle me-3" src="https://dummyimage.com/40x40/ced4da/6c757d" alt="..." />
                              <div class="small">
                                <div class="fw-bold">Kelly Rowan</div>
                                <div class="text-muted">March 12, 2021 &middot; 6 min read</div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
              </div>
            </section>
        </main>
    </template>
  </main-layout>
</template>

<script>
import MainLayout from "../layouts/MainLayout.vue"

export default {
  name: 'HomePage',
  components: {
    MainLayout
  },
}
</script>

<style>
</style>