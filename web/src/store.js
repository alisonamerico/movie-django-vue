import Vue from 'vue'
import Vuex from 'vuex'
import axios from './plugins/axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    token: null,
    movies: []
  },
  mutations: {
    SET_MOVIE (state, movies = []) {
      state.movies = movies
    },
    SET_LOGIN (state, auth) {
      state.user = auth.user
      state.token = auth.token
      localStorage.setItem('token', auth.token)
      axios.defaults.headers['Authorization'] = 'JWT ' + auth.token
    },
    SET_LOGOUT (state) {
      state.user = null
      state.token = null
      localStorage.clear()
      delete axios.defaults.headers['Authorization']
    }
  },
  actions: {
    postLogin: (context, credentials) => axios.post('rest-auth/login/', credentials)
      .then(
        res => context.commit('SET_LOGIN', res.data)
      ),
    verifyAuth: context => {
      const token = localStorage.getItem('token')

      if (token) {
        axios.defaults.headers['Authorization'] = 'JWT ' + token
      }

      return axios.get('rest-auth/user/')
    },
    loadMovies: context => axios.get('api/movies/').then(
      res => {
        context.commit('SET_MOVIE', res.data)
      }
    )
  }
})
