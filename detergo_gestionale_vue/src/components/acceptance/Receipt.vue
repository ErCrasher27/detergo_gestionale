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
                <th>Cliente: Fabrizia Bucci</th>
                <th>Data restituzione: 12/01/2005</th>
                <th>Note: questo scontrino è urgente perchè il cliente deve andare ad una cerimonia</th>
            </tr>
            <tr>
                <th><button class="button">Clienti</button></th>
                <th><button class="button">Restituzione</button></th>
                <th><button class="button">note</button></th>
            </tr>
        </tfoot>
        <tbody v-for="item in $store.state.items">
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.water_price}}</td>
                <td>{{item.water_price}}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>
</script>