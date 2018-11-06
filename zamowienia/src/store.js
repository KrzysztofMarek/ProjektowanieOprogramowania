import Vuex from 'vuex';
import Vue from 'vue';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        order: [],
    },
    mutations: {
        add_product(state, product) {
            state.order.push(product);
        },

        clear_order(state) {
            state.order = [];
        }
    }
})