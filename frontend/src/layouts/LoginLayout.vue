<template>
  <main class="d-flex w-100">
		<div class="container d-flex flex-column">
			<div class="row vh-100">
				<div class="col-sm-10 col-md-8 col-lg-6 mx-auto d-table h-100">
					<div class="d-table-cell align-middle">

						<div class="card">
              <div class="card-header bg-primary text-center">
                <span class="h2 mb-0 text-white">Login</span>
              </div>
							<div class="card-body">
								<div class="m-sm-4">
									<form @submit.prevent="login">
										<div class="mb-3">
											<label class="form-label">Email</label>
											<input class="form-control form-control-lg" type="email" name="email" placeholder="Email" v-model="email" required/>
										</div>
										<div class="mb-3">
											<label class="form-label">Senha</label>
											<input class="form-control form-control-lg" type="password" name="password" placeholder="Senha" v-model="password" required/>
											<small class="ms-2">
                        <a href="#">Esqueceu a senha?</a>
                      </small>
										</div>
										<div class="mb-3" v-if="loginError">
											<div class="alert alert-danger" role="alert">
												{{ loginError }}
											</div>
										</div>
										<div>
											<label class="form-check">
                      </label>
										</div>
										<div class="ms-auto text-end">
											<button type="submit" class="btn btn-lg btn-primary">Login</button>
										</div>
									</form>
								</div>
							</div>
						</div>

					</div>
				</div>
			</div>
		</div>
	</main>
</template>

<script>
export default {
	data() {
		return {
			email: '',
			password: '',
		}
	},
	computed: {
		loginError() {
			return this.$store.getters['authentication/getLoginError']
		},
	},
	methods: {
		login() {
			this.$store.dispatch({
        type: 'authentication/login',
				email: this.email,
				password: this.password
      })
		}
	},
	mounted() {
		if (this.$store.state.authentication.loggedStatus) {
			this.$router.go(-1)
		}
	}
}
</script>

<style>

</style>