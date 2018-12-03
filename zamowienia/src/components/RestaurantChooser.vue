<template>
    <v-container fluid fill-height>
        <v-layout align-center justify-center column>
        <v-alert :value="error_text.length != 0">{{ error_text }}</v-alert>
            <v-flex xs12 sm8 md4>
                <v-combobox
                    v-model="miasto_selected"    
                    :items="miasta"
                    label="Wybierz miasto"
                ></v-combobox>
            </v-flex>
            <v-flex xs12 sm8 md4>
                <v-combobox
                    v-model="restauracja_selected"    
                    :items="restauracje"
                    item-text="nazwa"
                    label="Wybierz restauracje"
                    return-object
                ></v-combobox>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import { oferty } from "../backend";

export default {
    name: "RestauranChooser",
    data: () => ({
        miasta: [],
        restauracje: [],
        miasto_selected: "",
        restauracja_selected: null,
        miasta_is_loading: true,
        restauracje_is_loading: false,
        error_text: "",
    }),
    created() {
        let self = this;
        oferty
            .get("/pobierz_miasta")
            .then((response) => {
                self.miasta_is_loading = false;
                self.miasta = response.data;
            })
            .catch((err) => {
                self.miasta_is_loading = false;
                if (err.response) {
                    self.error_text = `${err.response.status}: ${err.response.data}`;
                } else if (err.request) {
                    self.error_text = "Network error";
                    console.error(err);
                    self.miasta = ["Warszawa"];
                } else {
                    self.error_text = "Unexpected error";
                    console.error(err);
                }
            });
    },
    watch: {
        miasto_selected: function(miasto, old) {
            this.restauracje_is_loading = true;
            let self = this;
            oferty
                .get(`/pobierz_restrauracje_z_miasta?miasto=${miasto}`)
                .then((response) => {
                    self.restauracje_is_loading = false;
                    self.restauracje = response.data.lista;
                })
                .catch((err) => {
                    self.restauracje_is_loading = false;
                    if (err.response) {
                        self.error_text = `${err.response.status}: ${err.response.data}`;
                    } else if (err.request) {
                        self.error_text = "Network error";
                        console.error(err);
                        self.restauracje = [{ id_restauracji: 0, nazwa: "Cafe:Student", adres: "" }];
                    } else {
                        self.error_text = "Unexpected error";
                        console.error(err);
                    }
                });
        },
        restauracja_selected: function(restauracja, old) {
            this.$store.commit("set_restaurant", restauracja.id_restauracji);
            this.$router.push(`/browse`);
        },
    }
}
</script>
