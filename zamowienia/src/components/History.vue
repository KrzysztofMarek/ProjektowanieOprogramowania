<template>
    <v-container>
        <v-alert :value="error_text.length != 0">{{ error_text }}</v-alert>
        <v-layout justify-center>
            <v-flex xs12 lg6 my-2>
                <h3>Twoje zamówienia:</h3>
                <v-data-table
                    :items="orders"
                    class="elevation-1"
                    hide-actions
                    hide-headers
                >
                    <template slot="items" slot-scope="props">
                        <td>
                            <p class="text-truncate font-weight-medium" style="max-width:600px">{{ order_list_display(props.item) }}</p>
                            <p class="text-uppercase ">
                                {{ props.item.status}}
                                <v-btn v-if="props.item.status == 'oczekujace'" small>anuluj</v-btn>
                                <v-btn v-else small>ponów</v-btn>
                            </p>
                        </td>
                        <td class="text-xs-right">{{ display_price(props.item.kwota) }}</td>
                    </template>
                </v-data-table>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import { zamowienia } from "../backend";

export default {
    data: () => {
        return {
            error_text: "",
            is_loading: false,
            orders: [
                {
                    id_restauracji: 0,
                    lista: [{
                        id_dania: 0,
                        nazwa: "Pierogi",
                    }],
                    kwota: 10.0,
                    status: "dostarczone"
                },
                {
                    id_restauracji: 0,
                    lista: [
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                        {
                            id_dania: 0,
                            nazwa: "Pierogi",
                        },
                    ],
                    kwota: 200.0,
                    status: "oczekujace"
                }
            ],
        }},
    methods: {
        display_price: function(price) {
            return price + " zł";
        },
        order_list_display(order) {
            const dania = order.lista;
            let i = 0;
            let s = "";
            while (i + 1 < dania.length) {
                s += dania[i].nazwa + ", ";
                i += 1;
            }

            s += dania[i].nazwa;

            return s;
        }
    },
}
</script>

