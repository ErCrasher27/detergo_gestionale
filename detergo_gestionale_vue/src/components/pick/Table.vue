<template>
    <div class="table-container">
        <table class="table">
            <div v-for="category in categories">
                <Item :item="items"></Item>
            </div>
        </table>
    </div>
</template>

<script>
import axios from 'axios'
import Item from './Item.vue'
export default {
    props: {
        tab: {
            type: String,
            required: true
        }
    },
    components: {
        Item
    },
    data() {
        return {
            items: [],
        }
    },
    mounted() {
        this.getItem()
    },
    methods: {
        getItem() {
            axios
                .get('/api/v1/itemByCategory/')
                .then(response => {
                    this.items = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
}
</script>