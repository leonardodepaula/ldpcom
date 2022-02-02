<template>
  <div class="container d-flex flex-column">
			<div class="row">
				<div class="col-6 mx-auto d-table">
					<div class="d-table-cell align-middle">
						<div class="card">
							<div class="card-body mt-5 mb-5">
								<div class="text-center">
									<i class="align-middle icon-size-alert" data-feather="alert-circle"></i><span class="align-middle font-alert ms-4">Erro <b>404</b></span>
									<p class="h3 mt-3">
										Página não encontrada.
									</p>
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
  name: 'PageNotFound',
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