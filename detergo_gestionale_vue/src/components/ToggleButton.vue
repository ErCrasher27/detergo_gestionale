<!-- ToggleButton Component
    Accepts a parameter (defaultValue) for button selection, which can have the following values:
        "acceptance"
        "return"
    if you pass a parameter other than those indicated, it will not have any clicks
    and will assume the value of the passed value (which will not be treated)
-->

<template>
    <div class="toggle-container">
        <div>
            <input type="radio" name="toggle" id="toggle-acceptance" class="toggle toggle-acceptance" value="acceptance"
                v-model="checkedValue">
            <label for="toggle-acceptance" class="btn">ACCETTAZIONE</label>
        </div>
        <div>
            <input type="radio" name="toggle" id="toggle-return" class="toggle toggle-return" value="return"
                v-model="checkedValue">
            <label for="toggle-return" class="btn">RESTITUZIONE</label>
        </div>
    </div>

    <div>
        {{ currentState }}
    </div>
</template>

<script>
export default {
    props: {
        operation: {
            type: String,
            default: "acceptance"
        }
    },

    data() {
        return {
            currentState: this.operation
        }
    },

    computed: {
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

input[type="radio"].toggle:checked+label {
    cursor: default;
    color: #ffffff;
    background: #004A7E;
    border-bottom: 2px solid #004A7E;
}

input[type="radio"].toggle.toggle-acceptance:checked+label::before {
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    font-size: x-large;
    content: "\f291";
    margin-right: 8px;
}

input[type="radio"].toggle.toggle-return:checked+label::after {
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    font-size: x-large;
    content: "\e05d";
    margin-left: 8px;
}
</style>