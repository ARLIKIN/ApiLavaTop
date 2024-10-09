from datetime import datetime
from typing import List


class PartnerSaleDto(BaseModel):
    currency: Currency
    count: int = Field(...,description='Количество проданных экземпляров')
    amountTotal: int = Field(..., description='Общие продажи')


class ReportsResponses(BaseModel):
    productId: str = Field(..., description='Идентификатор продукта')
    title: str = Field(..., description='Название продукта')
    status: ContractStatusDto = Field(..., description='Статус продукта')
    sales: list[PartnerSaleDto]


class PartnerSaleDetailsDto(BaseModel):
    id: str = Field(..., description="Идентификатор контракта")
    created: datetime = Field(..., description="Дата создания")
    status: ContractStatusDto
    amountTotal: AmountTotalDto
    buyer: BuyerDto


class PartnerSalesPageDto(BaseModel):
    items: List[PartnerSaleDetailsDto] = Field(..., description="Элементы страницы")
    total: int = Field(..., description="Общее количество элементов")
    page: int = Field(..., description="Номер текущей страницы")
    size: int = Field(..., description="Максимальное количество элементов на странице")
    totalPages: int = Field(..., description="Общее количество страниц")


class Reports(BaseModel):
    items: List[ReportsResponses]
    total: int = Field(..., description='Общее количество элементов')
    page: int = Field(..., description='Номер текущей страницы')
    size: int = Field(
        ...,
        description='Максимальное количество элементов на странице'
    )
    totalPages: int = Field(..., description='Общее количество страниц')