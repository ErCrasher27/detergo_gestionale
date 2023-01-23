<template>
    <th><button @click="isShowModal = true" class="button">Clienti</button></th>
    <div class="modal" v-bind:class="{ 'is-active': isShowModal }">
        <div class="modal-background" v-on:click="isShowModal = false"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">Titolo</p>
                <button class="delete" aria-label="close" v-on:click="isShowModal = false"></button>
            </header>
            <section class="modal-card-body">
                <div class="field">
                    <div class="control is-large is-loading">
                        <input type="text" class="input is-large" placeholder="Filtra per codice, nome o telefono"
                            v-model="filter" />
                    </div>
                </div>
                <table class="table is-striped is-hoverable">
                    <thead>
                        <th>Codice</th>
                        <th>Nome e Cognome</th>
                        <th>Telefono</th>
                    </thead>
                    <tbody>
                        <tr v-for="row in filteredRows">
                            <td v-html="highlightMatches(row.id)"></td>
                            <td v-html="highlightMatches(row.name)"></td>
                            <td v-html="highlightMatches(row.last_name)"></td>
                            <td v-html="highlightMatches(row.phone)"></td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td><button @click="addNewCustomer = !addNewCustomer" class="button">Nuovo Cliente</button>
                            </td>
                        </tr>
                    </tfoot>
                </table>
                <div v-if="addNewCustomer">
                    <div class="field">
                        <label class="label">Nome</label>
                        <div class="control">
                            <input class="input" type="text" placeholder="Inserisci nome">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Cognome</label>
                        <div class="control">
                            <input class="input" type="text" placeholder="Inserisci nome">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Numero di telefono</label>
                        <div class="control has-icons-left has-icons-right">
                            <input class="input is-success" type="text" placeholder="Text input" value="bulma">
                            <span class="icon is-small is-left">
                                <i class="fas fa-phone"></i>
                            </span>
                            <span class="icon is-small is-right">
                                <i class="fas fa-check"></i>
                            </span>
                        </div>
                        <p class="help is-success">Questo numero di cellulare/fisso è corretto</p>
                    </div>
                    <div class="field">
                        <label class="label">Email</label>
                        <div class="control has-icons-left has-icons-right">
                            <input class="input is-danger" type="email" placeholder="Email input" value="hello@">
                            <span class="icon is-small is-left">
                                <i class="fas fa-envelope"></i>
                            </span>
                            <span class="icon is-small is-right">
                                <i class="fas fa-exclamation-triangle"></i>
                            </span>
                        </div>
                        <p class="help is-danger">This email is invalid</p>
                    </div>

                    <div class="field">
                        <label class="label">Note</label>
                        <div class="control">
                            <textarea class="textarea" placeholder="Inserisci note"></textarea>
                        </div>
                    </div>

                    <div class="field is-grouped">
                        <div class="control">
                            <button class="button is-link">Submit</button>
                        </div>
                        <div class="control">
                            <button class="button is-link is-light">Cancel</button>
                        </div>
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
import axios from 'axios'
import { response } from 'express';
export default {
    data() {
        return {
            isShowModal: false,
            customers: [],
            filter: "",
            addNewCustomer: false,
        }
    },
    mounted() {
        this.getCustomers()
    },
    watch: {
        search: function (searchValue) {
            this.searchValue = searchValue;
        }
    },
    computed: {
        filteredRows() {
            return this.customers.filter(row => {
                const id = row.id.toString().toLowerCase();
                const name = row.name.toLowerCase();
                const lastName = row.last_name.toLowerCase();
                const phone = row.phone.toLowerCase();
                const searchTerm = this.filter.toLowerCase();
                return (
                    id.includes(searchTerm) || name.includes(searchTerm) || lastName.includes(searchTerm) || phone.includes(searchTerm)
                );
            });
        }
    },
    methods: {
        getCustomers() {
            axios
                .get('/api/v1/customers/')
                .then(response => {
                    this.customers = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        postCustomer() {
            axios
                .post('/api/v1/customers/')
                .then(response => {
                    console.log(response.data)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        highlightMatches(text) {
            const textToString = text.toString();
            const matchExists = textToString.toLowerCase().includes(this.filter.toLowerCase());
            if (!matchExists) return textToString;
            const re = new RegExp(this.filter, "ig");
            return textToString.replace(re, matchedText => `<strong>${matchedText}</strong>`);
        }
    },
}
</script>