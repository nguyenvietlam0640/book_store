<!-- <template>
    <div>
        <StripeCheckout ref="checkoutRef" mode="payment" :pk="publishableKey" :line-items="line_items"
            :success-url="success_url" :cancel-url="cancel_url" :phone-number-colection="phone_number_collection"
            :shippingAddressCollection="shipping_address_collection" :shipping-options="shipping_options"
            @loading="v => loading = v" />
        <button @click="submit">Pay now!</button>
    </div>
</template>
  
<script>
import { StripeCheckout } from '@vue-stripe/vue-stripe';
export default {
    name: 'CheckoutView',
    components: {
        StripeCheckout,
    },
    data() {
        return {
            publishableKey: 'sk_test_51MnmhMI4tXTMcUFe5lg6uOLLOBB1z6NJocie3BnW1ZVCnWWKCD00LA601MHROcqjEcL1nR1l3shlNOCyAkxxihPa009AOwOwQd',
            loading: false,
            line_items: [{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': 2000,
                    'product_data': {
                        'name': 'book',
                        'images': ['https://upload.wikimedia.org/wikipedia/commons/b/b6/Gutenberg_Bible%2C_Lenox_Copy%2C_New_York_Public_Library%2C_2009._Pic_01.jpg']
                    },
                },
                'quantity': 2,
            }],
            success_url: 'http://localhost:8080/success',
            cancel_url: 'http://localhost:8080/cancel',
            phone_number_collection: {
                'enabled': true
            },
            shipping_address_collection: {
                "allowed_countries": ["VN"]
            },
            shipping_options: [
                {
                    "shipping_rate_data": {
                        "type": "fixed_amount",
                        "fixed_amount": { "amount": 500, "currency": "usd" },
                        "display_name": "Free shipping",
                        "delivery_estimate": {
                            "minimum": { "unit": "business_day", "value": 10 },
                            "maximum": { "unit": "business_day", "value": 15 },
                        },
                    },
                },
            ],
        };
    },
    methods: {
        submit() {
            // You will be redirected to Stripe's secure checkout page
            this.$refs.checkoutRef.redirectToCheckout();
        },
    },
};
</script> -->

<template>
    <div>
        <stripe-checkout ref="checkoutRef" mode="payment" :pk="publishableKey" :line-items="lineItems"
            :phone-number-colection="phone_number_collection" 
            :success-url="successURL" :cancel-url="cancelURL" @loading="v => loading = v" />
        <button style="padding-top: 200px;" @click="submit">Pay now!</button>
    </div>
</template>
  
<script>
import { StripeCheckout } from '@vue-stripe/vue-stripe'
export default {
    components: {
        StripeCheckout,
    },
    data() {
        this.publishableKey = 'pk_test_51MnmhMI4tXTMcUFeaBPq2vHoQvsufUsWiCs4gUyMqyOnkItW8LCUL18KEUGSQBZwuWlgausncJzaNQALYhcIY6s1006g0Ou456'
        return {
            loading: false,
            lineItems: [
                {
                    price: 'price_1Mo2VXI4tXTMcUFeiad1SWDX', // The id of the one-time price you created in your Stripe dashboard
                    quantity: 1,
                },
            ],
            successURL: 'http://localhost:8080/success',
            cancelURL: 'http://localhost:8080/cancel',
            phone_number_collection: {
                'enabled': true
            },
            
        };
    },
    methods: {
        submit() {
            // You will be redirected to Stripe's secure checkout page
            this.$refs.checkoutRef.redirectToCheckout()
        },
    },
};
</script>