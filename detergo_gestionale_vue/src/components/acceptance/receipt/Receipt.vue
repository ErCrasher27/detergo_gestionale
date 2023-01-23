<template>
    <table class="table is-hoverable">
        <thead>
            <tr>
                <th>Articolo</th>
                <th>Lavaggio</th>
                <th>Prezzo</th>
            </tr>
        </thead>
        <tfoot>
            <tr>
                <th>Tot. pezzi: 4</th>
                <th></th>
                <th>Tot. Euro: 30</th>
            </tr>
            <tr>
                <th>{{ $store.state.customer[0].name }}</th>
                <th>Data restituzione: 12/01/2005</th>
                <th>Note: questo scontrino è urgente perchè il cliente deve andare ad una cerimonia</th>
            </tr>
            <tr>
                <th>
                    <Customers></Customers>
                </th>
                <th>
                    <PickDate></PickDate>
                </th>
                <th>
                    <Notes></Notes>
                </th>
            </tr>
        </tfoot>
        <tbody v-for="item in $store.state.items">
            <tr>
                <td>{{ item.name }}</td>
                <td>{{ item.water_price }}</td>
                <td>{{ item.water_price }}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import Customers from './Customers.vue'
import PickDate from './PickDate.vue'
import Notes from './Notes.vue'
export default {
    components: {
        Customers,
        PickDate,
        Notes
    }
}
</script>