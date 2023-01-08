<template>
    <div class="table-container">
        <table class="table">
            <div v-for="item in itemsByCategory">
                <Item :item = item></Item>
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
            itemsByCategory: [],
        }
    },
    watch: {
        tabId(){
            this.getItemByCategory()
        }
    },
    methods: {
        getItemByCategory() {
            axios
                .get('/api/v1/itemByCategory/' + this.tabId + '/')
                .then(response => {
                    console.log(response.data)
                    this.itemsByCategory = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>