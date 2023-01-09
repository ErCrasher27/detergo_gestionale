<template>
    <div class="card is-flex is-flex-direction-column is-align-items-center" v-on:click="isShowModal = true">
        <span class="icon is-large">
            <img :src="item.get_icon" alt="ds">
        </span>
        <div class="card-content">
            <div class="media">
                <div class="media-content">
                    <p class="title is-6 has-text-centered">{{ item.name }}</p>
                </div>
            </div>
        </div>
    </div>

    <div class="modal" v-bind:class="{ 'is-active': isShowModal }">
        <div class="modal-background" v-on:click="isShowModal = false"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">{{item.name}}</p>
                <button class="delete" aria-label="close" v-on:click="isShowModal = false"></button>
            </header>
            <section class="modal-card-body">
                Modal Content
            </section>
            <footer class="modal-card-foot">
                <button class="button" v-on:click="isShowModal = false">Annulla</button>
                <button class="button">Aggiungi</button>
            </footer>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        item: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            isShowModal: false

        }
    }
}
</script>

<style scoped>
.card {
    margin: 0.5rem;
}

.card-content {
    padding: 0.5rem
}

.icon.is-large {
    height: 4rem;
    width: 4rem;
}
</style>