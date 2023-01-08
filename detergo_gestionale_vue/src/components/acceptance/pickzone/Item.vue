<template>
    <div class="card is-flex is-flex-direction-column is-align-items-center">
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
</template>

<script>
export default {
    props: {
        item: {
            type: Object,
            required: true
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