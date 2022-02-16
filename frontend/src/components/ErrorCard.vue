<template>
  <div class="container main-layout-container d-flex flex-column">
		<div class="row">
			<div class="col-6 mx-auto d-table">
				<div class="d-table-cell align-middle">
					<div class="card">
						<div class="card-body mt-5 mb-5">
							<div class="text-center">
								<font-awesome-icon icon="exclamation-circle" size="6x"/>
								<p class="align-middle font-alert mt-2 mb-1">Erro <b>{{ errorCode }}</b></p>
								<p class="h3 mt-0">
									{{ errorMessage }}
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

<script>

export default {
  name: 'ErrorCard',
	props: ['errorCode', 'errorMessage'],
	methods: {
    goBack() {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>

.card-alert {
	margin: 400px;
}

.icon-size-alert {
	width: 50px;
	height: 50px;
}

.font-alert {
	font-size: 50px;
}

</style>