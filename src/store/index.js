import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    error: '', // error: {header: header, description: description, level: info | success | error}
  },
  mutations: {
    SET_ERROR: (state, payload) => {
      state.error = payload
    }
  },
  getters: {
    ERROR: state => {
      return state.error
    }
  },
  actions: {
  },
  modules: {
  }
})
