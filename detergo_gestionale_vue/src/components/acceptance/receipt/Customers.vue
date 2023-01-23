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
                        <th>Nome</th>
                        <th>Cognome</th>
                        <th>Telefono</th>
                    </thead>
                    <tbody>
                        <tr v-for="row in filteredRows" @click="idRowSelected = row.id"
                            :class="{ 'is-selected': idRowSelected == row.id }">
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
                <form @submit.prevent="insertCustomer()">
                    <div v-if="addNewCustomer">
                        <div class="field is-horizontal">
                            <div class="field-body">
                                <div class="field">
                                    <label class="label">Nome</label>
                                    <p class="control is-expanded has-icons-left">
                                        <input class="input" type="text" placeholder="Nome" v-model="name">
                                        <span class="icon is-small is-left">
                                            <i class="fas fa-user"></i>
                                        </span>
                                    </p>
                                </div>
                                <div class="field">
                                    <label class="label">Cognome</label>
                                    <p class="control is-expanded has-icons-left">
                                        <input class="input" type="text" placeholder="Cognome" v-model="lastName">
                                        <span class="icon is-small is-left">
                                            <i class="fas fa-user"></i>
                                        </span>
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div class="field is-horizontal">
                            <div class="field-body">
                                <div class="field">
                                    <label class="label">Numero di telefono</label>
                                    <div class="control has-icons-left has-icons-right">
                                        <input class="input"
                                            :class="{ 'is-success': isValidPhone(), 'is-danger': !isValidPhone() }"
                                            type="text" placeholder="Inserisci numero di telefono" v-model="phone">
                                        <span class="icon is-small is-left">
                                            <i class="fas fa-phone"></i>
                                        </span>
                                        <span v-if="!isValidPhone()" class="icon is-small is-right">
                                            <i class="fas fa-exclamation-triangle"></i>
                                        </span>
                                    </div>
                                    <p v-if="isValidPhone()" class="help is-success">Il numero di telefono inserito è
                                        valido!
                                    </p>
                                    <p v-if="!isValidPhone()" class="help is-danger">Il numero di telefono inserito non
                                        è
                                        valido!
                                    </p>
                                </div>
                                <div class="field">
                                    <label class="label">Email</label>
                                    <div class="control has-icons-left has-icons-right">
                                        <input class="input"
                                            :class="{ 'is-success': isValidEmail(), 'is-danger': !isValidEmail() }"
                                            type="email" placeholder="Email" v-model="email">
                                        <span class="icon is-small is-left">
                                            <i class="fas fa-envelope"></i>
                                        </span>
                                        <span v-if="!isValidEmail()" class="icon is-small is-right">
                                            <i class="fas fa-exclamation-triangle"></i>
                                        </span>
                                    </div>
                                    <p v-if="isValidEmail()" class="help is-success">L'email inserita è valida!</p>
                                    <p v-if="!isValidEmail()" class="help is-danger">L'email inserita non è valida!</p>
                                </div>
                            </div>
                        </div>
                        <div class="field">
                            <label class="label">Indirizzo</label>
                            <div class="control">
                                <input class="input" type="text" placeholder="Inserisci indirizzo" v-model="address">
                            </div>
                        </div>
                        <div class="field">
                            <label class="label">Note</label>
                            <div class="control">
                                <textarea class="textarea" placeholder="Note" v-model="notes"></textarea>
                            </div>
                        </div>
                        <div class="notification is-danger" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                        <div class="field">
                            <div class="control">
                                <button class="button is-link">Salva</button>
                            </div>
                        </div>
                    </div>
                </form>
            </section>
            <footer class="modal-card-foot">
                <button class="button" v-on:click="isShowModal = false">Annulla</button>
                <button @click="$store.dispatch('setCustomerToReceipt', getCustomerByIdAndCloseModal(idRowSelected))"
                    class="button">Aggiungi</button>
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
            filter: "",
            idRowSelected: null,
            addNewCustomer: false,
            name: null,
            lastName: null,
            phone: null,
            email: null,
            address: null,
            notes: null,
            errors: []
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
        insertCustomer() {
            this.errors = []
            if (this.name === '') {
                this.errors.push('Il nome è obbligatorio')
            }
            if (this.lastName === '') {
                this.errors.push('Il cognome è obbligatorio')
            }
            if (this.phone === '') {
                this.errors.push('Il numero di telefono è obbligatorio')
            }
            if (!this.errors.length) {
                const formData = {
                    name: this.name,
                    last_name: this.lastName,
                    phone: this.phone,
                    email: this.email,
                    address: this.address,
                    notes: this.notes,
                }
                axios
                    .post("/api/v1/customers/", formData)
                    .then(response => {
                        console.log(response)
                        this.getCustomers()
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Qualcosa è andato storto. Perfavore riprova di nuovo.')
                            console.log(JSON.stringify(error))
                        }
                    })
            }
        },
        highlightMatches(text) {
            const textToString = text.toString();
            const matchExists = textToString.toLowerCase().includes(this.filter.toLowerCase());
            if (!matchExists) return textToString;
            const re = new RegExp(this.filter, "ig");
            return textToString.replace(re, matchedText => `<strong>${matchedText}</strong>`);
        },
        getCustomerByIdAndCloseModal(id) {
            this.isShowModal = false
            return this.customers
                .filter(customer => [id].includes(customer.id))
        },
        isValidEmail() {
            return /^[^@]+@\w+(\.\w+)+\w$/.test(this.email);
        },
        isValidPhone() {
            return /^\d{10}$/.test(this.phone);
        },
    },
}
</script>