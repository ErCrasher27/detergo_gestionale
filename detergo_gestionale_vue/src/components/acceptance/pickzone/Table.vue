<template>
    <div class="is-flex is-flex-direction-row is-flex-wrap-wrap	is-justify-content-flex-start">
        <div v-for="item in itemsByCategory">
            <Item :item=item></Item>
        </div>
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
        tabId() {
            this.getItemByCategory()
        }
    },
    methods: {
        getItemByCategory() {
            axios
                .get('/api/v1/itemsByCategory/' + this.tabId + '/')
                .then(response => {
                    this.itemsByCategory = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>