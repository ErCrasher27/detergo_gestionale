import { createStore } from 'vuex'

export default createStore({
  state: {
    items: [],
    customer: Object,
    isLoading: false
  },
  getters: {
    items: function (state) {
      return `${state.items}`
    },
    customer: function (state) {
      return `${state.customer}`
    }
  },
  mutations: {
    UPDATE_RECEIPT_ITEMS(state, payload) {
      state.items = payload
    },
    UPDATE_RECEIPT_CUSTOMER(state, payload) {
      state.customer = payload
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
  },
  actions: {
    addToReceipt(context, payload) {
      const items = context.state.items
      items.push(payload)
      context.commit('UPDATE_RECEIPT_ITEMS', items)
    },
    setCustomerToReceipt(context, payload) {
      var customer = context.state.customer
      customer = payload
      context.commit('UPDATE_RECEIPT_CUSTOMER', customer)
    }
  },
  modules: {
  }
})
