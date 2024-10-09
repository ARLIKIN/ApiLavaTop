# Пример использования клиента
import asyncio

from LavaTopPayment import (
    LavaTop,
    Currency,
    PaymentMethod,
    Language,
    WebhookEventTypeDto,
    WebhookAuthRequest,
    WebhookAuthTypeDto
)

TOKEN = 'TOKEN'


async def main():
    client = LavaTop(api_key=TOKEN)
    products = await client.get_products()
    print(products)
    invoice = await client.create_invoice(
        email='email@gmail.com',
        offer_id='uuid',
        currency=Currency.RUB,
        payment_method=PaymentMethod.BANK131,
        buyer_language=Language.RU
    )
    print(invoice)
    payment = await client.get_product_by_id(invoice.id)
    print(payment)
    reports = await client.get_sales()
    print(reports)
    reports_id = await client.get_sales_by_product(products.items[0].id)
    print(reports_id)
    donate = await client.get_donate_link()
    print(donate)
    webhook = await client.create_webhook(
        url='google.com',
        name='Test Webhook',
        api_key_id='api_key',
        event_type=WebhookEventTypeDto.PAYMENT_RESULT,
        auth_config= WebhookAuthRequest(authType=WebhookAuthTypeDto.NONE)
    )
    print(webhook)
    history_webhook = await client.get_webhook_history()
    print(history_webhook)



if __name__ == '__main__':
    pass
    asyncio.run(main())

