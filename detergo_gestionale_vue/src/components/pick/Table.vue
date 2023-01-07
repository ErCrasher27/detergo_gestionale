<template>
    <div class="table-container">
        <table class="table">
            <div v-for="item in items">
                <Item :item="items.name"></Item>
            </div>
        </table>
    </div>
</template>

<script>
import axios from 'axios'
import Item from './Item.vue'
export default {
    props: {
        tabId: {
            type: Number,
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
                .get('/api/v1/itemByCategory/' + this.tabId + '/')
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