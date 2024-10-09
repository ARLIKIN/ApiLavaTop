from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from datetime import datetime

from LavaTopPayment.models.types import WebhookAuthTypeDto, WebhookEventTypeDto


class WebhookAuthRequest(BaseModel):
    """Авторизационные данные для вебхука на сервисе партнёра"""
    authType: WebhookAuthTypeDto
    authValue: Optional[str] = Field(
        None,
        description="Ключ для авторизации. Пусто только в случае с authType == 'none'"
    )


class WebhookCreateRequest(BaseModel):
    url: str
    name: str
    apiKeyId: str
    eventType: WebhookEventTypeDto
    authConfig: Optional[WebhookAuthRequest]


class WebhookResponse(BaseModel):
    id: str
    name: str
    apiKeyId: str
    url: str
    eventType: WebhookEventTypeDto
    isActive: bool
    authType: WebhookAuthTypeDto
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class WebhookUpdateRequest(BaseModel):
    url: str
    isActive: bool
    name: str
    eventType: WebhookEventTypeDto
    authConfig: Optional[WebhookAuthRequest] = None


class ErrorResponse(BaseModel):
    error: str
    details: Optional[Dict[str, str]]
    timestamp: datetime = None


class WebhookDeliveryResponse(BaseModel):
    id: str
    webhookId: str
    isDelivered: bool
    deliveredAt: Optional[datetime] = None
    lastDeliveryAttemptAt: Optional[datetime] = None
    responseStatus: Optional[int] = None
    createdAt: datetime


class WebhookHistoryResponse(BaseModel):
    items: List[WebhookDeliveryResponse] = Field(...,description="Элементы страницы")
    total: int = Field(..., description="Общее количество элементов")
    page: int = Field(..., description="Номер текущей страницы")
    size: int = Field(..., description="Максимальное количество элементов на странице")
