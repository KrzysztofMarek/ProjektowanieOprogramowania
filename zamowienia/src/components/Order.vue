<template>
    <v-container>
        <v-alert :value="error_text.length != 0">{{ error_text }}</v-alert>
        <v-layout justify-center>
            <v-flex xs12 lg6 my-2>
                <h3>Zamówienie:</h3>
                <v-data-table
                    :items="$store.state.order"
                    class="elevation-1"
                    hide-actions
                    hide-headers
                >
                    <template slot="items" slot-scope="props">
                        <td>{{ props.item.nazwa }}</td>
                        <td class="text-xs-right">{{ display_price(props.item.cena) }}</td>
                    </template>
                </v-data-table>
            </v-flex>
        </v-layout>
        <v-layout justify-center text-xs-right>
            <v-flex xs12 lg6>
                <strong>Razem: {{ display_price(total_price) }}</strong>
                <v-dialog v-model="points_dialog" width="500">
                    <v-btn slot="activator" flat small>wykorzystaj punkty</v-btn>
                    <v-card>
                        <v-card-title
                            class="headline"
                            primary-title
                        >
                            Wykorzystaj punkty lojalnościowe
                        </v-card-title>
                        <v-card-text>
                            Nie masz żadnych punktów do wykorzystania.
                        </v-card-text>
                        <v-card-actions>
                            <v-btn
                                flat
                                @click="points_dialog = false"
                            >
                                Anuluj
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </v-flex>
        </v-layout>
        <v-layout justify-center>
            <v-flex xs12 lg6 my-2>
                <v-form v-model="valid">
                    <v-text-field
                        v-model="name"
                        :rules="name_rules"
                        :counter="20"
                        label="Imię"
                        required
                    />
                    <v-text-field
                        v-model="surname"
                        :rules="surname_rules"
                        :counter="30"
                        label="Nazwisko"
                        required
                    />
                    <v-text-field
                        v-model="email"
                        :rules="email_rules"
                        label="E-mail"
                        required
                    />
                    <v-text-field
                        v-model="phone"
                        :rules="phone_rules"
                        label="Telefon"
                        required
                    />
                    <v-textarea
                        v-model="address"
                        :rules="address_rules"
                        :counter="200"
                        label="Adres"
                        required
                    />
                </v-form>
            </v-flex>
        </v-layout>
        <v-layout justify-center>
            <v-flex xs6 lg3>
                <v-checkbox label="Akceptuję regulamin restauracji" v-model="is_tos_accepted"></v-checkbox>
            </v-flex>
            <v-flex d-flex align-center xs3 lg1>
                <v-btn to="/browse">Wróć</v-btn>
            </v-flex>
            <v-flex d-flex align-center xs3 lg1>
                <v-btn color="error" @click='$store.commit("clear_order")'>Wyczyść</v-btn>
            </v-flex>
            <v-flex d-flex align-center xs3 lg1>
                <v-btn :loading="is_loading" color="primary" :disabled="!order_active" @click="create_order">Zamów</v-btn>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import { zamowienia } from "../backend";
import XRegExp from "xregexp";

function phone_length_validator(s) {
    let arr = s.split("");
    let n_count = arr.filter(c => RegExp('[0-9]').test(c)).length;

    if (s.length != 0 && s[0] == '+') {
        return n_count == 11 || "Nieprawidłowa długość telefonu";
    } else {
        return n_count == 9 || n_count == 11 || n_count == 13
            || "Nieprawidłowa długość telefonu";
    }
}

export default {
    data: () => {
        let only_letter = XRegExp('^\\p{L}+$');
        return {
            is_tos_accepted: false,
            error_text: "",
            is_loading: false,
            valid: false,
            points_dialog: false,
            name: "",
            name_rules: [
                v => !!v || "Imię jest wymagane",
                v => v.length <= 20 || "Imię jest za długie",
                v => only_letter.test(v) || "Tylko litery",
                v => (v[0] && v[0] == v[0].toUpperCase()) || "Imię musi zaczynać się z dużej litery",
            ],
            surname: "",
            surname_rules: [
                v => !!v || "Nazwisko jest wymagane",
                v => v.length <= 30 || "Nazwisko jest za długie",
                v => only_letter.test(v) || "Tylko litery",
               // v => (v[0] && v[0] == v[0].toUpperCase()) || "Nazwisko musi zaczynać się z dużej litery",
            ],
            email: "",
            email_rules: [
                v => !!v || "E-mail jest wymagane",
                v => RegExp('^.+@.+\\..+$').test(v) || "Nieprawidłowy adres email"
            ],
            phone: "",
            phone_rules: [
                v => !!v || "Telefon jest wymagane",
                v => RegExp('\\+{0,1}[0-9 ].+').test(v) || "Tylko +, cyfry i spacje",
                phone_length_validator,
            ],
            address: "",
            address_rules: [
                v => !!v || "Adres jest wymagany",
            ],
        }},
    methods: {
        display_price: function(price) {
            return price + " zł";
        },
        create_order: function() {
            this.is_loading = true;
            let self = this;
            let zamowienie = {
                id_klienta: 0,
                id_restauracji: this.$store.state.restaurant.id_restauracji,
                lista_dan: this.$store.state.order.map(v => { return { id_dania: v.id_dania, nazwa: v.nazwa }}),
                kwota: this.total_price,
                adres: this.address,
            };
            zamowienia
                .post("/dodaj_zamowienie", zamowienie)
                .then((response) => {
                    self.is_loading = false;
                    if (response.data.redirect == undefined) {
                        self.$router.push("/history");
                    } else {
                        window.location.href = response.data.redirect;
                    }
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
        }
    },
    computed: {
        total_price: function() {
            return this.$store.state.order.reduce((sum, val) => sum + val.cena, 0);
        },
        order_active: function() {
            return this.valid && this.$store.state.order.length != 0 && this.is_tos_accepted
        }
    }
}
</script>

