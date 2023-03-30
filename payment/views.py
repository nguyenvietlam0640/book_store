from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse
import stripe
from rest_framework.views import APIView, Response
domain = 'https://lamnv-bookstore.netlify.app'

stripe.api_key = 'sk_test_51MnmhMI4tXTMcUFe5lg6uOLLOBB1z6NJocie3BnW1ZVCnWWKCD00LA601MHROcqjEcL1nR1l3shlNOCyAkxxihPa009AOwOwQd'

endpoint_secret = 'whsec_28815ee5db79bdd31d32f0231d661c02ba4c9d41d215764bfe7fa07145c52640'


@csrf_exempt
def webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Save an order in your database, marked as 'awaiting payment'
        create_order(session)

        # Check if the order is already paid (for example, from a card payment)
        #
        # A delayed notification payment will have an `unpaid` status, as
        # you're still waiting for funds to be transferred from the customer's
        # account.
        if session.payment_status == "paid":
            # Fulfill the purchase
            fulfill_order(session)

    elif event['type'] == 'checkout.session.async_payment_succeeded':
        session = event['data']['object']

        # Fulfill the purchase
        fulfill_order(session)

    elif event['type'] == 'checkout.session.async_payment_failed':
        session = event['data']['object']

        # Send an email to the customer asking them to retry their order
        email_customer_about_failed_payment(session)

    # Passed signature verification
    return HttpResponse(status=200)


def fulfill_order(session):
    # TODO: fill me in
    print('fill', session)


def create_order(session):
    # TODO: fill me in
    print('create', session)


def email_customer_about_failed_payment(session):
    # TODO: fill me in
    print('fail', session)


class create_checkout_session(APIView):
    def post(self, request):
        try:

            checkout_session = stripe.checkout.Session.create(

                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(float(item['book']['unit_price'])*100),
                        'product_data': {
                            'name': item['book']['title'],
                            'images': [item['book']['get_image']]
                        },
                    },
                    'quantity': int(item['quantity']),
                } for item in request.data['items']],
                mode='payment',
                success_url='http://localhost:8080/success',
                cancel_url='http://localhost:8080/cancel',
                phone_number_collection={
                    'enabled': True
                },
                shipping_address_collection={
                    "allowed_countries": ["VN"]},
                shipping_options=[
                    {
                        "shipping_rate_data": {
                            "type": "fixed_amount",
                            "fixed_amount": {"amount": 500, "currency": "usd"},
                            "display_name": "Free shipping",
                            "delivery_estimate": {
                                "minimum": {"unit": "business_day", "value": 10},
                                "maximum": {"unit": "business_day", "value": 15},
                            },
                        },
                    },
                ],

            )

        except Exception as e:
            return str(e)

        return Response({'checkout_session_url': checkout_session.url})
