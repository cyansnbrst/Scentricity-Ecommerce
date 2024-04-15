import {createStore} from 'vuex';

export default createStore({
    state: {
        backendURL: 'http://127.0.0.1:8000/api/v1',
        authToken: null,
    },
    mutations: {
        setAuthToken(state, token) {
            state.authToken = token;
        },
        clearAuthToken(state) {
            state.authToken = null;
        }
    },
    actions: {
        async changeCart(context, {product_id, action}) {
            await fetch(
                `${context.state.backendURL}/cart/change/${action}/${product_id}/`, {
                    method: 'PUT',
                    headers: {
                        'Authorization': `Token ${context.state.authToken}`
                    }
                }).then(response => response)
        }
    },
    getters: {
        getServerUrl: state => state.backendURL,
        isLoggedIn: state => !!state.authToken,
    }
});
