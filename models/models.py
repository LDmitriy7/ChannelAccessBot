from typing import Optional

from pydantic import BaseModel

import texts


class Tariff(BaseModel):
    id: int
    title: str
    description: str
    price: int
    duration: Optional[int]
    channel_id: Optional[int]


tariffs = [
    Tariff(
        id=1,
        title='🎉 Доступ навсегда',
        description=texts.tariff1_description,
        price=379,
        channel_id=-1001558897531,
    ),
    Tariff(
        id=2,
        title='🔥 Премиум доступ',
        description=texts.tariff2_description,
        price=589,
        channel_id=-1001558897531,
    )
]
