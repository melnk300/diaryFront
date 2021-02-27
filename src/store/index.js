import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    error: {}, // error: {header: header, description: description, level: info | success | error}
    isReg: 0
  },
  mutations: {
    SET_ERROR: (state, payload) => {
      state.error = payload
    },
    SET_ISREG: (state, payload) => {
      state.isReg = payload 
    }
  },
  getters: {
    ERROR: state => {
      return state.error
    },
    ISREG: state => {
      return state.isReg
    }
  },
  actions: {
  },
  modules: {
  }
})
