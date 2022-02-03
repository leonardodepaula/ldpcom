<template>
  <main-layout>
    <template v-slot:content>
      <div class="container d-flex flex-column">
        <div class="row">
          <div class="card card-out mb-3 mt-3 pt-3">
            <div class="card-body text-center">
              <img src="../assets/img/leonardodepaula.jpg" alt="Christina Mason" class="img-fluid rounded-circle mb-2" width="200" height="80" />
              <h2 class="mb-0">Leonardo de Paula</h2>
            </div>
            <hr class="my-0" />
            <div class="card-body">
              <div class="ml-2">
                <div class="row">
                  <strong><font-awesome-icon icon="book" /> Educação</strong>
                </div>
                <div class="row mt-2">
                  <span class="text-muted">
                    Graduação em Direito | Pontifícia Universidade Católica de Goiás (PUC-GO)
                    <br>Pós-graduação em Direito Tributário | Escola Nacional de Administração Pública (Enap)
                  </span>
                </div>
              </div>
            </div>
            <hr class="my-0" />
            <div class="card-body">
              <div class="ml-2">
                <div class="row">
                  <strong><font-awesome-icon icon="briefcase" /> Trabalho</strong>
                </div>
                <div class="row mt-2">
                  <span class="text-muted">
                    Auditor-Fiscal da Receita Federal
                  </span>
                </div>
              </div>
            </div>
            <hr class="my-0" />
            <div class="card-body">
              <div class="ml-2">
                <div class="row">
                  <strong><font-awesome-icon icon="lightbulb" /> Interesses</strong>
                </div>
                <div class="row mt-2">
                  <span class="text-muted">
                    Python 
                    <br>Web Development | Django | FastAPI | Vue.js | NGINX
                    <br>Bancos de dados | SQL | MariaDB | PostgreSQL
                    <br>Containers | Docker
                    <br>Data Science | Machine Learning | Numpy | Pandas | Scikit-Learn
                    <br>Direito Tributário | Conformidade tributária
                    <br>Linux | Fedora | Red Hat downstream distributions | Gnome
                  </span>
                </div>
              </div>
            </div>
            <hr class="my-0" />
            <div class="card-body">
              <div class="ml-2">
                <div class="row">
                  <strong><font-awesome-icon icon="network-wired" /> Perfis</strong>
                </div>
                <div class="mt-2 text-center">
                  <a href="https://github.com/leonardodepaula" target="_blank">
                    <button class="btn mt-3 p-3" type="button">
                      <font-awesome-icon :icon="['fab', 'github']" size="4x"/>
                      <br>
                      <p class="h4 mt-2 mb-0">GitHub</p>
                    </button>
                  </a>

                  <a href="https://www.kaggle.com/leonardodepaula" target="_blank">
                    <button class="btn mt-3 p-3 ml-3" type="button">
                      <font-awesome-icon :icon="['fab', 'kaggle']" size="4x"/>
                      <br>
                      <p class="h4 mt-2 mb-0">Kaggle</p>
                    </button>
                  </a>

                  <a href="https://www.linkedin.com/in/leonardodepaulaliebscher" target="_blank">
                    <button class="btn mt-3 p-3 ml-3" type="button">
                      <font-awesome-icon :icon="['fab', 'linkedin']" size="4x"/>
                      <br>
                      <p class="h4 mt-2 mb-0">LinkedIn</p>
                    </button>
                  </a>
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
  name: 'Biography',
  components: {
    MainLayout
  },
}
</script>

<style>
</style>