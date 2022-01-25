<template>
  <div class="wrapper">
		<SideBar />

		<div class="main">
			
			<NavBar />

			<main class="content">
				<router-view></router-view>
			</main>

			<footer class="footer">
				<div class="container-fluid">
					<div class="row text-muted">
						<div class="col-6 text-start">
							<p class="mb-0">
								<strong>leonardodepaula.com</strong>
							</p>
						</div>
						<div class="col-6 text-end">
							<ul class="list-inline">
								<li class="list-inline-item">
									<span>LdP</span>
								</li>
							</ul>
						</div>
					</div>
				</div>
			</footer>
		</div>
	</div>
</template>

<script>

import SideBar from "../components/SideBar.vue"
import NavBar from "../components/NavBar.vue"

export default {
  name: 'IndexView',
  components: {
		SideBar,
		NavBar,
  },
}
</script>

<style>
</style>