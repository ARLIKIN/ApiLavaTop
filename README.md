# ApiLavaTop
Библиотека для платежной системы Lava.top

1. Авторизация, либо по api_key либо по username password

       client = LavaTop(api_key=TOKEN)
       client = LavaTop(username='<LOGIN>', password='<PASSWORD>')

2. Получение всех продуктов

       products = await client.get_products()
       print(products)

3. Создание платежа, в offer_id укажите id товара полученного из продукта 
   ● Если стоимость продукта указана в рублях, 
   то картой МИР, Visa или MasterCard российских банков.

   ● Если стоимость продукта указана в евро или долларах, 
   то картой Visa или MasterCard иностранных банков. 
   Если к карте привязан счёт не в долларах или евро, то при 
   оплате стоимость конвертируется по курсу банка. 
   Банк может взимать за это комиссию.

       invoice = await client.create_invoice(
           email='email@gmail.com',
            offer_id='uuid',
            currency=Currency.RUB,
            payment_method=PaymentMethod.BANK131,
            buyer_language=Language.RU
       )

4. Получение платежа по id и проверка платежа

       payment = await client.get_product_by_id(invoice.id)
       if payment.status == 'completed':
            print('completed')
       print(payment)


### Разработчик:
* [**ARLIKIN**](https://github.com/ARLIKIN)
