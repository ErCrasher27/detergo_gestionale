<!-- tabs in alto, dentro delle card... per quanto riguarda lo scontrino -> table -->
<template>
    <div class="block">
        <div class="tabs is-toggle is-fullwidth is-large">
            <ul>
                <li class="is-active">
                    <a>
                        <span class="icon"><i class="fas fa-image" aria-hidden="true"></i></span>
                        <span>Appendibili</span>
                    </a>
                </li>
                <li>
                    <a>
                        <span class="icon"><i class="fas fa-music" aria-hidden="true"></i></span>
                        <span>Non Appendibili</span>
                    </a>
                </li>
                <li>
                    <a>
                        <span class="icon"><i class="fas fa-film" aria-hidden="true"></i></span>
                        <span>Fabrizie</span>
                    </a>
                </li>
                <li>
                    <a>
                        <span class="icon"><i class="far fa-file-alt" aria-hidden="true"></i></span>
                        <span>Varie</span>
                    </a>
                </li>
            </ul>
        </div>
    </div>

    <div>
        {{ categorie }}
    </div>

</template>

<script>
import axios from 'axios'

export default {
    name: 'Home',

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
                    console.log(response)
                    this.categorie = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>
