
<template>
    <v-container>
        <v-layout justify-center>
            <v-flex xs12 sm10 my-2>
                <h3>Potrawy:</h3>
                <v-data-iterator
                    :items="dishes"
                    content-tag="v-layout"
                    content-props="row wrap justify-start"
                >
                    <v-flex
                        slot="item"
                        slot-scope="props"
                        xs12
                        sm3
                        mx-2
                    >
                        <v-card>
                            <v-img
                                src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Japanese_Raw_Aonori_Misoshiru.JPG/1024px-Japanese_Raw_Aonori_Misoshiru.JPG"
                                aspect-ratio="2.0"
                            ></v-img>

                            <v-card-title primary-title>
                                <div>
                                    <h3 class="headline mb-0">{{ props.item.nazwa }}</h3>
                                    <div>{{ props.item.opis }}</div>
                                </div>
                            </v-card-title>

                            <v-card-actions>
                                <v-btn color="primary" @click="$store.commit('add_product', props.item)">{{ display_price(props.item.cena) }} </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-flex>
                </v-data-iterator>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import { oferty } from "../backend";

export default {
    name: "Browse",
    data: () => ({
        dishes: [
            {
                id_dania: 0,
                nazwa: "Zupa miso",
                cena: 10,
                opis: "Pyszna zupa miso",
            },
            {
                id_dania: 1,
                nazwa: "Pierogi z serem",
                cena: 8,
                opis: "Zestaw ośmiu pierogów z serem",
            }
        ]
    }),
    created() {
        let self = this;
        oferty
            .get(`Pobierz_menu_restauracji?id_restauracji=${this.$store.state.restaurant.id_restauracji}`)
            .then((response) => {
                self.dishes = response.data.lista;
            })
    },
    methods: {
        display_price: function(price) {
            return price + " zł";
        }
    },
    computed: {
    }
}
</script>

