import { createStore } from 'vuex'

export default createStore({
  state: {
    items: [],
    isLoading: false
  },
  getters: {
    items: function (state) {
      return `${state.items}`
    }
  },
  mutations: {
    UPDATE_RECEIPT(state, payload) {
      state.items = payload
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
  },
  actions: {
    addToReceipt(context, payload) {
      const items = context.state.items
      items.push(payload)
      context.commit('UPDATE_RECEIPT', items)
    }
  },
  modules: {
  }
})
