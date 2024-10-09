class Donate(BaseModel):
    url: str = Field(..., description='Ссылка на окно доната автора')