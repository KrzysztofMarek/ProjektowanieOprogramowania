import Vuex from 'vuex';
import Vue from 'vue';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        order: [],
        current_restaurant: null,
        address: "",
    },
    mutations: {
        add_product(state, product) {
            state.order.push(product);
        },

        set_order(state, order) {
            state.order = order;
        },

        clear_order(state) {
            state.order = [];
        },

        set_restaurant(state, restaurant) {
            state.current_restaurant = restaurant
        },

        set_address(state, address) {
            state.address = address
        },
    }
})