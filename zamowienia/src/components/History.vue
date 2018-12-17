<template>
    <v-container>
        <v-alert :value="error_text.length != 0">{{ error_text }}</v-alert>
        <v-dialog v-model="rating_dialog" width="500">
            <v-card>
                <v-card-title
                    class="headline"
                    primary-title
                >
                    Oceń realizację zamówienia
                </v-card-title>
                <v-card-text>
                    <p>Jak bardzo jesteż zadowolony z realizacji zamówienia?</p>
                    <rate v-model="rating_editing" />
                </v-card-text>
                <v-card-actions>
                    <v-spacer />
                    <v-btn
                        flat
                        @click="rating_dialog = false"
                    >
                        Anuluj
                    </v-btn>
                    <v-btn
                        flat
                        :disabled="rating_editing == null"
                        @click="save_rating()"
                    >
                        Oceń
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <v-layout justify-center>
            <v-flex xs12 lg6 my-2>
                <h3>Twoje zamówienia:</h3><br />
                <v-data-table
                    :items="orders"
                    class="elevation-1"
                    hide-headers
                    :loading="is_loading"
                >
                    <template slot="items" slot-scope="props">
                        <td>
                            <p class="text-truncate font-weight-medium" style="max-width:420px;margin-top:7px">{{ order_list_display(props.item) }}</p>
                            <p class="text-uppercase ">
                                {{ props.item.status }}
                                <v-dialog v-if="props.item.status == 'oczekujace'" v-model="cancel_dialog" width="500">
                                    <v-btn slot="activator" small>Anuluj</v-btn>
                                    <v-card>
                                        <v-card-title
                                            class="headline"
                                            primary-title
                                        >
                                            Anuluj zamówienie
                                        </v-card-title>
                                        <v-card-text>
                                            Czy na pewno chcesz anulować zamówienie <strong>{{ order_list_display(props.item) }}</strong>?
                                        </v-card-text>
                                        <v-card-actions>
                                            <v-spacer />
                                            <v-btn
                                                flat
                                                @click="cancel_dialog = false"
                                            >
                                                Nie
                                            </v-btn>
                                            <v-btn
                                                flat
                                                @click="cancel_order(props.item.id_zamowienia)"
                                            >
                                                Tak
                                            </v-btn>
                                        </v-card-actions>
                                    </v-card>
                                </v-dialog>
                                <v-btn v-else-if="props.item.status == 'dostarczone'" small @click="repeat_order(props.item)">ponów</v-btn>
                                <v-btn v-else-if="props.item.status == 'anulowane'" small @click="repeat_order(props.item)">ponów</v-btn>

                                <template v-if="props.item.status == 'dostarczone' && props.item.ocena == null">
                                    <v-btn small color="primary" @click="edit_rating(props.index)">Oceń</v-btn>
                                </template>
                                <template v-else-if="props.item.ocena != null">
                                    <span class="font-weight-medium" style="font-size:1.2rem">{{props.item.ocena / 2.0}}/5</span>
                                </template>
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
import { zamowienia, oferty } from "../backend";
import Rate from "./Rate";

export default {
    data: () => {
        return {
            error_text: "",
            is_loading: true,
            cancel_dialog: false,
            rating_dialog: false,
            rating_editing: 0,
            order_editing_idx: 0,
            orders: [],
        }},
    methods: {
        display_price: function(price) {
            return price + " zł";
        },
        edit_rating(idx) {
            this.rating_editing = this.orders[idx].ocena;
            this.rating_editing_idx = idx;
            this.rating_dialog = true;
        },
        save_rating() {
            this.orders[this.rating_editing_idx].ocena = this.rating_editing;
            let order = this.orders[this.rating_editing_idx];
            this.rating_dialog = false;

            let self = this;
            zamowienia.post(`/dodaj_ocene_zamowienia?id_zamowienia=${order.id_zamowienia}&ocena=${order.ocena}`)
                .catch((err) => {
                    if (err.response) {
                        self.error_text = `${err.response.status}: ${err.response.data}`;
                    } else if (err.request) {
                        self.error_text = "Network error";
                        console.error(err);
                    } else {
                        self.error_text = "Unexpected error";
                        console.error(err);
                    }
                });
        },
        order_list_display(order) {
            const dania = order.lista_dan;
            let i = 0;
            let s = "";
            while (i + 1 < dania.length) {
                s += dania[i].nazwa + ", ";
                i += 1;
            }

            s += dania[i].nazwa;

            return s;
        },
        cancel_order(id_zamowienia) {
            let self = this;
            zamowienia
                .post(`/zmien_staus_zamowienia?id_zamowienia=${id_zamowienia}&status=anulowane`)
                .then((response) => {
                    self.cancel_dialog = false;
                })
                .catch((err) => {
                    if (err.response) {
                        self.error_text = `${err.response.status}: ${err.response.data}`;
                    } else if (err.request) {
                        self.error_text = "Network error";
                        console.error(err);
                    } else {
                        self.error_text = "Unexpected error";
                        console.error(err);
                    }
                });
        },
        repeat_order: async function(order) {
            try {
                const menu_response = await oferty.get(`/pobierz_menu_restauracji?id_restauracji=${order.id_restauracji}`);
                const menu = menu_response.data.lista;
                const new_order = order.lista_dan.map(o => menu.find(x => x.id_dania == o.id_dania)).filter(x => x != undefined);
                this.$store.commit('set_order', new_order);
                this.$store.commit('set_restaurant', order.id_restauracji);
                this.$store.commit('set_address', order.adres);
                this.$router.push("/checkout");
            } catch (err) {
                this.error_text = "Nie udało się ponowić zamówienia";
                console.error(err);
            }
        },
        test(a) {
            console.log(a)
        }
    },
    created: function() {
        let self = this;
        zamowienia
            .get("/pobierz_liste_zamowien?id_klienta=0")
            .then((response) => {
                self.is_loading = false;
                self.orders = response.data.lista_zamowien;
            })
            .catch((err) => {
                self.is_loading = false;
                if (err.response) {
                    self.error_text = `${err.response.status}: ${err.response.data}`;
                } else if (err.request) {
                    self.error_text = "Network error";
                    console.error(err);
                } else {
                    self.error_text = "Unexpected error";
                    console.error(err);
                }
            });
    },
    components: {
        rate: Rate,
    },
}
</script>

