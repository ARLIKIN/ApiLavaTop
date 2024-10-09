from datetime import datetime

import httpx
from typing import Optional, Dict, Any

from models.donate import Donate
from models.products import Invoice, ProductsResponse
from models.reports import Reports, PartnerSalesPageDto
from models.types import Currency, PaymentMethod, Language
from models.webhooks import WebhookResponse, WebhookEventTypeDto, \
    WebhookAuthRequest, WebhookHistoryResponse


class LavaTop:
    def __init__(self, api_key: Optional[str] = None,
                 token: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None):
        self.base_url = 'https://gate.lava.top'
        self.api_key = api_key
        self.token = token
        self.auth = (username, password) if username and password else None
        self.headers = {}

        if api_key:
            self.headers["X-Api-Key"] = api_key
        if token:
            self.headers["Authorization"] = f"Bearer {token}"
    #region Webhooks
    async def create_webhook(
        self,
        url: str,
        name: str,
        api_key_id: str,
        event_type: WebhookEventTypeDto,
        auth_config: Optional[WebhookAuthRequest] = None,
    ) -> WebhookResponse:
        """
        Создание вебхука.
        :param url: URL сервиса, который будет принимать запросы
        :param name: Имя
        :param api_key_id: Соответствующий API ключ
        :param event_type: Тип вебхука
        :param auth_config: Авторизационные данные для вебхука на сервисе партнёра
        :return: WebhookResponse
        """
        url_path = f"{self.base_url}/api/v1/webhooks"
        data = {
            'url': url,
            'name': name,
            'apiKeyId': api_key_id,
            'eventType': event_type,
        }
        if auth_config is not None:
            data['authConfig'] = auth_config.model_dump()
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url_path, json=data,
                headers=self.headers,
                auth=self.auth
            )
            response.raise_for_status()
            return WebhookResponse(**response.json())

    async def get_webhooks(self) -> WebhookResponse:
        """
        Получить вебхуки партнёра
        :return: WebhookResponse
        """
        url = f"{self.base_url}/api/v1/webhooks"
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=self.headers,
                auth=self.auth
            )
            response.raise_for_status()
            return WebhookResponse(**response.json())

    async def get_webhook_history(
        self,
        page: Optional[int] = None,
        size: Optional[int] = None
    ) -> WebhookHistoryResponse:
        """
        Получение информации о вебхуке по ID.
        :param page: Номер страницы
        :param size: Количество возвращаемых элементов страницы
        :return:
        """
        url = f"{self.base_url}/api/v1/webhook-history"
        params = {}

        if page is not None:
            params["page"] = page
        if size is not None:
            params["size"] = size
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=self.headers,
                params=params,
                auth=self.auth
            )
            response.raise_for_status()
            return WebhookHistoryResponse(**response.json())

    async def update_webhook(
        self,
        webhook_id: str,
        url: str = None,
        is_active: Optional[bool] = None,
        name: str = None,
        event_type: WebhookEventTypeDto = None,
        auth_config: Optional[WebhookAuthRequest] = None,
    ) -> WebhookResponse:
        """
        Обновление вебхука по ID.
        :param str webhook_id: Идентификатор вебхука
        :param str url: URL сервиса, который будет принимать запросы
        :param bool is_active: Активен ли вебхук
        :param str name: Имя
        :param WebhookEventTypeDto event_type: Тип вебхука
        :param WebhookAuthRequest auth_config: Авторизационные данные для вебхука на сервисе партнёра
        :return:
        """
        url_path = f"{self.base_url}/api/v1/webhooks/{webhook_id}"
        data = {
            'url': url,
            'isActive': is_active,
            'name': name,
            'eventType': event_type,
        }
        if auth_config is not None:
            data['authConfig'] = auth_config.model_dump()
        async with httpx.AsyncClient() as client:
            response = await client.put(
                url_path,
                json=data,
                headers=self.headers,
                auth=self.auth
            )
            response.raise_for_status()
            return WebhookResponse(**response.json())

    async def delete_webhook(self, webhook_id: str) -> None:
        """
        Удаление вебхука по ID.
        :param webhook_id:
        :return:
        """
        url = f"{self.base_url}/api/v1/webhooks/{webhook_id}"
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                url,
                headers=self.headers,
                auth=self.auth
            )
            response.raise_for_status()
    #endregion

    #region Products
    async def get_products(self) -> ProductsResponse:
        """
        Метод для получения списка продуктов.
        """
        url = f"{self.base_url}/api/v2/products"
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=self.headers,
                auth=self.auth
            )
            response.raise_for_status()
            data = response.json()
            return ProductsResponse(**data)

    async def create_invoice(
        self,
        email: str,
        offer_id: str,
        currency: Currency,
        payment_method: PaymentMethod,
        buyer_language: Optional[Language] = None
    ) -> Invoice:
        """
        Создание контракта на покупку контента.
        :param str email: Почта покупателя
        :param str offer_id: Идентификатор цены
        :param Currency currency: Валюта
        :param PaymentMethod payment_method: Тип оплаты
        :param Optional[Language] buyer_language: Язык пользователя
        :return: Invoice
        """
        url = f"{self.base_url}/api/v2/invoice"
        json_data = {
            "email": email,
            "offerId": offer_id,
            "currency": currency,
            "paymentMethod": payment_method,
        }
        if buyer_language is not None:
            json_data["buyerLanguage"] = buyer_language
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json=json_data,
                headers=self.headers,
                auth=self.auth
            )
            response.raise_for_status()
            return Invoice(**response.json())

    async def get_product_by_id(
        self,
        payment_id: str
    ) -> Invoice:
        """
        Метод для получения платежа по ID.
        :param payment_id: ID платежа
        :return: Invoice
        """
        url = f"{self.base_url}/api/v1/invoice?id={payment_id}"
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=self.headers,
                auth=self.auth
            )
            response.raise_for_status()
            return Invoice(**response.json())

    async def update_product_v2(
        self,
        product_id: str,
        product_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Метод для обновления продукта.
        :param product_id:
        :param product_data:
        :return:
        """
        url = f"{self.base_url}/api/v2/products/{product_id}"
        async with httpx.AsyncClient() as client:
            response = await client.put(
                url,
                json=product_data,
                headers=self.headers,
                auth=self.auth
            )
            response.raise_for_status()
            return response.json()
    #endregion

    #region Subscriptions
    async def cancel_subscription(self, contract_id: str, email: str) -> None:
        url = f"{self.base_url}/api/v1/subscriptions"
        params = {
            "contractId": contract_id,
            "email": email
        }
        async with httpx.AsyncClient() as client:
            response = await client.delete(url, params=params,
                                           headers=self.headers)
            response.raise_for_status()
            return None
    #endregion

    #region Reports
    async def get_sales(
        self,
        page: Optional[int] = None,
        size: Optional[int] = None
    ) -> Reports:
        """
        Получение списка продаж партнёра.
        :param int page: Номер страницы
        :param int size: Количество возвращаемых элементов страницы
        :return:
        """
        url = f"{self.base_url}/api/v1/sales"
        params = {}

        if page is not None:
            params["page"] = page
        if size is not None:
            params["size"] = size

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers,
                                        params=params)
            response.raise_for_status()  # Генерирует исключение при ошибке
            return Reports(**response.json())

    async def get_sales_by_product(
        self, product_id: str,
        page: Optional[int] = None,
        size: Optional[int] = None,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
        currency: Optional[str] = None,
        status: Optional[str] = None,
        search: Optional[str] = None
    ) -> PartnerSalesPageDto:
        """
        Получение списка продаж партнёра по конкретному продукту.
        :param str product_id: Идентификатор продукта
        :param int page: Номер страницы
        :param int size: Количество возвращаемых элементов страницы
        :param datetime from_date: Начало периода продаж (YYYY-MM-DDTHH:MM:SS+XX:XX)
        :param datetime to_date: Конец периода продаж (YYYY-MM-DDTHH:MM:SS+XX:XX)
        :param str currency: RUB, USD, EUR
        :param str status: Статус продажи: new, in-progress, completed, failed, cancelled, subscription-active, subscription-expired, subscription-cancelled, subscription-failed
        :param str search: Строка для поиска
        :return:
        """
        url = f"{self.base_url}/api/v1/sales/{product_id}"
        params = {}

        if page is not None:
            params["page"] = page
        if size is not None:
            params["size"] = size
        if from_date is not None:
            params["fromDate"] = from_date.isoformat() if from_date else None
        if to_date is not None:
            params["toDate"] = to_date.isoformat() if to_date else None
        if currency is not None:
            params["currency"] = currency
        if status is not None:
            params["status"] = status
        if search is not None:
            params["search"] = search

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers,
                                        params=params)
            response.raise_for_status()
            return PartnerSalesPageDto(**response.json())
    #endregion

    #region Donate
    async def get_donate_link(self) -> Donate:
        url = f"{self.base_url}/api/v1/donate"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            response.raise_for_status()
            return Donate(**response.json())
    #endregion


