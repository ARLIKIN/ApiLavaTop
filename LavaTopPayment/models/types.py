from enum import Enum

from pydantic import BaseModel, Field, EmailStr


# Перечисления для различных типов
class FeedItemType(str, Enum):
    POST = "POST"
    PRODUCT = "PRODUCT"

class ProductType(str, Enum):
    COURSE = "COURSE"
    DIGITAL_PRODUCT = "DIGITAL_PRODUCT"
    BOOK = "BOOK"
    GUIDE = "GUIDE"
    SUBSCRIPTION = "SUBSCRIPTION"
    AUDIO = "AUDIO"
    MODS = "MODS"
    CONSULTATION = "CONSULTATION"

class PostType(str, Enum):
    """Тип поста"""
    LESSON = "LESSON"
    POST = "POST"

class FeedVisibility(str, Enum):
    ALL = "ALL"
    ONLY_VISIBLE = "ONLY_VISIBLE"
    ONLY_HIDDEN = "ONLY_HIDDEN"

class Currency(str, Enum):
    """Валюта"""
    RUB = "RUB"
    USD = "USD"
    EUR = "EUR"

class ContractStatusDto(str, Enum):
    """Статус контракта."""
    NEW = "new"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    SUBSCRIPTION_ACTIVE = "subscription-active"
    SUBSCRIPTION_EXPIRED = "subscription-expired"
    SUBSCRIPTION_CANCELLED = "subscription-cancelled"
    SUBSCRIPTION_FAILED = "subscription-failed"

class Language(str, Enum):
    """Класс для представления языков."""
    EN = "EN"
    RU = "RU"
    ES = "ES"

class PaymentMethod(str, Enum):
    """Провайдер для платежа. Для платежей в российских рублях (RUB) доступен только BANK131, для платежей в Евро (EUR) или Долларах (USD) - UNLIMINT и PAYPAL."""
    BANK131 = "BANK131"
    UNLIMINT = "UNLIMINT"
    PAYPAL = "PAYPAL"


class AmountTotalDto(BaseModel):
    """Класс для представления общей суммы."""
    amount: float = Field(..., description="Общая сумма")
    currency: Currency = Field(..., description="Валюта")

class BuyerDto(BaseModel):
    email: str = Field(..., description="Почта покупателя")


class WebhookEventTypeDto(str, Enum):
    """
    Тип вебхука
    PAYMENT_RESULT='payment_result'
    RECURRENT_PAYMENT='recurrent_payment'
    """
    PAYMENT_RESULT='payment_result'
    RECURRENT_PAYMENT='recurrent_payment'


class WebhookAuthTypeDto(str, Enum):
    """
    Тип авторизации для вебхука.
    NONE='none'
    BASIS='basic'
    API_KEY='api_key'
    """
    NONE='none'
    BASIS='basic'
    API_KEY='api_key'