from typing import Optional

from models import models


def get_tariff(tariff_id: int) -> Optional[models.Tariff]:
    for tariff in models.tariffs:
        if tariff.id == tariff_id:
            return tariff
    return None
