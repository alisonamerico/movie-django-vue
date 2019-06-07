<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>The Movies</h3>
        </div>
      </div>
      <template v-for="movie in movies">
        <div :key="movie.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <movie-card :onDelete="deleteMovie" :movie="movie"></movie-card>
        </div>
      </template>
    </div>
  </main>
</template>
<script>
import MovieCard from "~/components/MovieCard.vue";
export default {
  head() {
    return {
      title: "Movies list"
    };
  },
  components: {
    MovieCard
  },
  async asyncData({ $axios, params }) {
    try {
      let movies = await $axios.$get(`/movies/`);
      return { movies };
    } catch (e) {
      return { movies: [] };
    }
  },
  data() {
    return {
      movies: []
    };
  },
  methods: {
    async deleteMovie(movie_id) {
      try {
        await this.$axios.$delete(`/movies/${movie_id}/`); 
        let newRecipes = await this.$axios.$get("/movies/");
        this.movies = newMovies;
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>
<style scoped>
</style>