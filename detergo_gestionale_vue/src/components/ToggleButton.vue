<!-- ToggleButton Component
    Accetta un parametro (defaultValue) per la selezione del pulsante, che può avere i seguenti valori: 
        "accettazione" 
        "restituzione"    
    se passi un parametro diverso da quelli indicati, non avrà alcun click 
    e assumerà il valore del valore passato (che non sarà trattato)
-->

<template>

    <div class="toggle-container">

        <div>
            <input type="radio" name="toggle" id="toggle-accettazione" class="toggle toggle-accettazione"
                value="accettazione" v-model="checkedValue">
            <label for="toggle-accettazione" class="btn">ACCETTAZIONE</label>
        </div>

        <div>
            <input type="radio" name="toggle" id="toggle-restituzione" class="toggle toggle-restituzione"
                value="restituzione" v-model="checkedValue">
            <label for="toggle-restituzione" class="btn">RESTITUZIONE</label>
        </div>

    </div>

    <span>value: {{ checkedValue }}</span>


</template>

<script>
export default {

    props: {
        defaultValue: {
            type: String,
            default: "accettazione"
        }
    },

    data() {
        return {
            currentState: this.defaultValue
        }
    },

    computed : {
        checkedValue: {
            get() {
                return this.currentState;
            },

            set(newValue) {
                this.currentState = newValue;
            }
        }
    }
}
</script>

<style scoped>
.toggle-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 497.14px;
    height: 87px;
    border-radius: 43px;
    background: #00A7E0;
    border-bottom: 3px solid #00A7E0;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.btn {
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    width: 248.57px;
    height: 87px;
    border-radius: 43px;
    color: rgba(255, 255, 255, 0.7);
    font-family: "Gunterz";
}

input[type="radio"].toggle {
    display: none;
}

input[type="radio"].toggle+label {
    cursor: pointer;
}

input[type="radio"].toggle+label:hover {}

input[type="radio"].toggle:checked+label {
    cursor: default;
    color: #ffffff;
    background: #004A7E;
    border-bottom: 2px solid #004A7E;
}

input[type="radio"].toggle.toggle-accettazione:checked+label::before {
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    font-size: x-large;
    content: "\f291";
    margin-right: 8px;
}

input[type="radio"].toggle.toggle-restituzione:checked+label::after {
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    font-size: x-large;
    content: "\e05d";
    margin-left: 8px;
}
</style>