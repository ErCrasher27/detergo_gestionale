<template>

  <div>
    <PickZone></PickZone>
  </div>


  <div class="block is-flex	is-justify-content-center	">
    <ToggleButton/>
  </div>

</template>

<script>
import ToggleButton from '../components/ToggleButton.vue'
import PickZone from '../components/PickZone.vue'

export default {
  name: 'App',

  components: {
    ToggleButton,
    PickZone
  },

}
</script>

<style>

</style>
