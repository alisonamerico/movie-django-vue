<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>The Movies</h3>
          <input type="text" v-model="search" placeholder="search movie..." />
          <router-link to="/" class="btn btn-info">Back Home</router-link>
        </div>
      </div>
      <template v-for="movie in filteredMovies">
        <div :key="movie.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <movie-card :onDelete="deleteMovie" :movie="movie"></movie-card>
        </div>
      </template>
    </div>
  </main>
</template>

<script>
export default {
  data(){
    return {
      search:''
    }
  },
  computed: {
    movies () {
      return this.$store.state.movies
    },
    filteredMovies: function(){
      return this.movies.filter((movie) => {
        return movie.movie_title.toLowerCase().match(this.search);
      });
    }
  },
  methods: {
    deleteMovie (movieId) {
      console.log('deleta ai')
    }
  },
  created () {
    this.$store.dispatch('verifyAuth')
  },
  mounted () {
    this.$store.dispatch('loadMovies')
  }
}
</script>
