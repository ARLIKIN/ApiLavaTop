from typing import List, Optional, Union
from datetime import datetime

from LavaTopPayment import *
from LavaTopPayment.models.types import *


# Модели данных
class PriceDto(BaseModel):
    """Сумма"""
    amount: Optional[float]
    currency: Currency

class OfferResponse(BaseModel):
    """Предложения для покупки продукта"""
    id: str
    name: Optional[str]
    description: Optional[str] = None
    prices: List[PriceDto]

class ProductItemResponse(BaseModel):
    id: str
    title: Optional[str]
    description: Optional[str] = None
    type: ProductType
    offers: Optional[List[OfferResponse]] = None

class PostItemResponse(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    body: str
    type: PostType
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
    publishedAt: Optional[datetime]

class ProductsResponse(BaseModel):
    items: List[Union[ProductItemResponse, PostItemResponse]]
    nextPage: Optional[str] = Field(
        default=None,
        description="Ссылка на следующую страницу постов и продуктов"
    )


class Invoice(BaseModel):
    id: str = Field(..., description="Идентификатор контракта на покупку")
    status: ContractStatusDto = Field(..., description="Статус контракта")
    amountTotal: AmountTotalDto = Field(..., description="Общая сумма")
    paymentUrl: Optional[str] = Field(
        None,
        description="Ссылка на виджет оплаты продукта (пусто, если продукт бесплатный)",
    )
