<!-- tabs in alto, dentro delle card... per quanto riguarda lo scontrino -> table -->
<template>
    <div class="tabs is-centered is-boxed is-medium">
        <ul>
            <li>
                <a>
                    <span class="icon is-small"><i class="fas fa-image" aria-hidden="true"></i></span>
                    <span>Pictures</span>
                </a>
            </li>
            <li class="is-active">
                <a>
                    <span class="icon is-small"><i class="fas fa-music" aria-hidden="true"></i></span>
                    <span>Music</span>
                </a>
            </li>
            <li>
                <a>
                    <span class="icon is-small"><i class="fas fa-film" aria-hidden="true"></i></span>
                    <span>Videos</span>
                </a>
            </li>
            <li>
                <a>
                    <span class="icon is-small"><i class="far fa-file-alt" aria-hidden="true"></i></span>
                    <span>Documents</span>
                </a>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            categorie: []
        }
    },

    components: {
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
