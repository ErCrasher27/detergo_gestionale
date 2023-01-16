<template>
  <div class="container is-fluid">
    <div class="columns is-centered">
      <div class="column is-4">
        <Tab maxi="LE"></Tab>
      </div>
      <div class="column is-4 is-flex is-justify-content-center">
        <Receipt></Receipt>
      </div>
      <div class="column is-4">
        <Tab maxi="RI"></Tab>
      </div>
    </div>
    <div class="is-flex is-justify-content-center">
      <MainSwitch></MainSwitch>
    </div>
  </div>
</template>

<script>
import Tab from '../components/acceptance/pickzone/Tab.vue'
import Receipt from '../components/acceptance/Receipt.vue'
import MainSwitch from '../components/MainSwitch.vue'
export default {
  components: {
    Tab,
    MainSwitch,
    Receipt
  },
}
</script>
