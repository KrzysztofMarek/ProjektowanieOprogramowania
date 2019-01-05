
<template>
<v-container fluid fill-height>
    <v-layout align-center justify-center>
        <v-flex xs12 sm10 md8>
            <v-card v-if="$route.query.success == '1'" class="elevation-12" color="light-green lighten-4">
                <v-card-text class="text-xs-center">
                    <h1 class="green--text text--darken-2 display-3 font-weight-light">Zamówienie numer {{ $route.params.id }} zostało złożone</h1>
                    <p>Niedługo je dostarczymy. W między czasie, możesz przejrzeć swoją <router-link to="/history">historię zamówień.</router-link></p>
                </v-card-text>
            </v-card>
            <v-card v-else class="elevation-12" color="red lighten-4">
                <v-card-text class="text-xs-center">
                    <h1 class="red--text text--darken-2 display-3 font-weight-light">Zamówienie numer {{ $route.params.id }} zostało anulowane</h1>
                    <p>Niestety nie udało nam się uzyskać pozytywnej odpowiedzi od systemu płatności. Twoje zamówienie zostało automatycznie anulowane,
                        możesz spróbować je ponowić w <router-link to="/history">historii zamówień.</router-link>
                    </p>
                </v-card-text>
            </v-card>
        </v-flex>
    </v-layout>
</v-container>
</template>

<script>

export default {
    name: "OrderCompleted",
    methods: {
    }
}
</script>