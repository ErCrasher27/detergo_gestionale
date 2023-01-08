<template>
    <div class="tabs is-centered is-boxed is-medium">
        <div v-for="category in categories">
            <ul>
                <li :class="{ 'is-active': tabId == category.id }">
                    <a @click="setCategory(category.id, category.name)">
                        <span class="icon is-small"><img :src="category.get_icon" alt=""></span>
                        <span>{{ category.name }}</span>
                    </a>
                </li>
            </ul>
        </div>
    </div>
    <div>
        <Table v-bind:tabId="tabId">
        </Table>
    </div>
</template>

<script>
import axios from 'axios'
import Table from './Table.vue'
export default {
    data() {
        return {
            categories: [],
            currentTabId: '',
            currentTabName: ''
        }
    },
    components: {
        Table
    },
    mounted() {
        this.getCategories()
    },
    methods: {
        setCategory(id, name) {
            this.tabId = id
            this.tabName = name
        },
        getCategories() {
            axios
                .get('/api/v1/categories/')
                .then(response => {
                    this.categories = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
    computed: {
        tabId: {
            get() {
                return this.currentTabId;
            },
            set(newValue) {
                this.currentTabId = newValue;
            }
        },
        tabName: {
            get() {
                return this.currentTabName;
            },
            set(newValue) {
                this.currentTabName = newValue;
            }
        }
    }
}
</script>

<style scoped>
</style>

