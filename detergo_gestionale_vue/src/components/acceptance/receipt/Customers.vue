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
                <div class="select">
                    <select @change="onChangeFindFor($event)">
                        <option value="1">cerca per id</option>
                        <option value="2">cerca per Nome e Cognome</option>
                        <option value="3">cerca per Telefono</option>
                    </select>
                </div>
                <div class="field">
                    <div class="control is-large is-loading">
                        <input v-model="search" class="input is-large" type="text" placeholder="cerca cliente">
                    </div>
                </div>
                <table class="table is-striped is-hoverable">
                    <thead>
                        <th>Codice</th>
                        <th>Nome e Cognome</th>
                        <th>Telefono</th>
                    </thead>
                    <tbody>
                        <tr v-for="customer in customers">
                            <td>{{ customer.id }}</td>
                            <td>{{ customer.name + ' ' + customer.last_name }}</td>
                            <td>{{ customer.phone }}</td>
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
export default {
    data() {
        return {
            isShowModal: false,
            customers: [],
            findFor: null,
            search: '',
            searchValue: '',
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
        onChangeFindFor(event) {
            this.findFor = event.target.value
            console.log(this.findFor)
        }
    },
}
</script>