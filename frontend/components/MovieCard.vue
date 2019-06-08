<template>
  <div class="card movie-card">
    <img :src="movie.picture" class="card-img-top" >
    <div class="card-body">
      <h5 class="card-title">{{ movie.movie_title }}</h5>
      <div class="action-buttons">
        <nuxt-link :to="`/movies/${movie.id}/`" class="btn btn-sm btn-success"> View </nuxt-link>
      </div>
    </div>
  </div>
</template>
<script>
export default {
    props: ["movie", "onDelete"]
};
</script>
<style>
.movie-card {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
}
</style>