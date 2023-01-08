<template>
    <div class="table-container">
        <table class="table">
            {{(tabId)}}
            <div v-for="item in itemsByCategory">
                {{tabId}}
            </div>
        </table>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    props: {
        tabId: {
            type: Number,
            required: true
        }
    },
    components: {
    },
    data() {
        return {
            itemsByCategory: [],
        }
    },
    watch: {
        tabId(){
            this.getItem()
        }
    },
    methods: {
        getItem() {
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