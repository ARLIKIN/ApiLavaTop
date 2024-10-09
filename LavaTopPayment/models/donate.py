from LavaTopPayment import *
from LavaTopPayment.models.types import *

class Donate(BaseModel):
    url: str = Field(..., description='Ссылка на окно доната автора')