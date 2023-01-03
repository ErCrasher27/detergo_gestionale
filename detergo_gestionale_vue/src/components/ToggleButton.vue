<template>

    <div class="toggle-container">

        <div>
            <input id="toggle-on" class="toggle toggle-left" name="toggle" value="false" type="radio" checked>
            <label for="toggle-on" class="btn label-btn">ACCETTAZIONE</label>
        </div>
        <div>
            <input id="toggle-off" class="toggle toggle-right" name="toggle" value="true" type="radio">
            <label for="toggle-off" class="btn label-btn">RESTITUZIONE</label>
        </div>

    </div>

</template>

<script>
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

.label-btn {
    font-family: "Gunterz";
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

input[type="radio"].toggle-left.toggle:checked+label::before {
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    font-size: x-large;
    content: "\f291";
    margin-right: 8px;
}

input[type="radio"].toggle-right.toggle:checked+label::after {
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    font-size: x-large;
    content: "\e05d";
    margin-left: 8px;
}
</style>