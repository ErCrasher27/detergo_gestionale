<!-- tabs in alto, dentro delle card... per quanto riguarda lo scontrino -> table -->
<template>
      <tabs :mode="mode">
        <tab title="Tab 1">Hello From Tab 1</tab>
        <tab title="Tab 2">Hello From Tab 2</tab>
        <tab title="Tab 3">Hello From Tab 3</tab>
        <tab title="Tab 4">Hello From Tab 4</tab>
      </tabs>
  </template>

<script>
import axios from 'axios'

import Tab from './Tab.vue'
import Tabs from './Tabs.vue'

export default {
    data() {
        return {
            categorie: []
        }
    },

    components: {
        Tab,
        Tabs
    },

    mounted() {
        this.getCategorie()
    },

    methods: {
        getCategorie() {
            axios
                .get('/api/v1/categorie/')
                .then(response => {
                    this.categorie = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>

<style lang="css">
</style>
