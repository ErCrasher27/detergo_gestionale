<template>
    <th><button @click="isShowModal = true" class="button">Note</button></th>

    <div class="modal" v-bind:class="{ 'is-active': isShowModal }">
        <div class="modal-background" v-on:click="isShowModal = false"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">Note</p>
                <button class="delete" aria-label="close" v-on:click="isShowModal = false"></button>
            </header>
            <section class="modal-card-body">
                <div class="field">
                    <div class="control">
                        <textarea class="textarea is-medium" placeholder="Medium textarea"></textarea>
                    </div>
                </div>
            </section>
            <footer class="modal-card-foot">
                <button class="button" v-on:click="isShowModal = false">Annulla</button>
                <button @click="$store.dispatch('addToReceipt', item)" class="button">Aggiungi</button>
            </footer>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            isShowModal: false
        }
    }
}
</script>