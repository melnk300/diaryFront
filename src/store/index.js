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
    ADD_ERROR: (context, payload) => {
      context.commit('SET_ERROR', payload)
      setTimeout(() => context.commit('SET_ERROR', ''), 3000)
    }
  },
  modules: {
  }
})
