<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3></h3>
          <router-link to="/movies" class="btn btn-info">Back List</router-link>
        </div>
      </div>
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ movie.movie_title }}</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img
          class="img-fluid"
          style="width: 300px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="movie.picture"
          alt
        >
      </div>
      <div class="col-md-6">
        <div class="movie-details">
          <h4>Movie Title</h4>
          <p>{{ movie.movie_title }}</p>
          <h4>Genres</h4>
          <p>{{ movie.genres }} mins</p>
          <h4>Duration ⏱</h4>
          <p>{{ movie.duration }}</p>
          <h4>Title Year</h4>
          <p>{{ movie.title_year }}</p>
          <h4>Director Name</h4>
          <p>{{ movie.director_name }}</p>
          <h4>Imdb Score</h4>
          <p>{{ movie.imdb_score }}</p>          
        </div>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  computed: {
    movie () {
      return this.$store.state.movie
    }
  },
async beforeMount () {
    await this.$store.dispatch('loadMovie', this.$route.params.id)
  }
}
</script>
<style scoped>
</style>