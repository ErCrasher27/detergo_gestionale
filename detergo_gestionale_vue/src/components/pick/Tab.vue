<template>
    <div class="tabs is-centered is-boxed is-medium">
        <div v-for="category in categories">
            <ul>
                <li :class="{ 'is-active': currentTab == category.name }">
                    <a @click="currentTab = category.name">
                        <span class="icon is-small"><i class="fas fa-image" aria-hidden="true"></i></span>
                        <span>{{ category.name }}</span>
                    </a>
                </li>
            </ul>
        </div>
    </div>
    <Table v-bind:tab="currentTab">
    </Table>
</template>

<script>
import axios from 'axios'
import Table from './Table.vue'
export default {
    data() {
        return {
            categories: [],
            tab: ''
        }
    },
    components: {
        Table
    },
    mounted() {
        this.getCategories()
    },
    methods: {
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
        currentTab : {
            get() {
                return this.tab;
            },
            set(newValue) {
                this.tab = newValue;
            }
        }
    }
}
</script>

