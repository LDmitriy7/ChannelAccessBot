from aiogram.types import InlineKeyboardMarkup
from aiogram_utils.keyboards import InlineKeyboardButton

from models import documents


class Tariffs(InlineKeyboardMarkup):
    TARIFF = InlineKeyboardButton('{title}', callback_data='tariff:{tariff_id}')

    def __init__(self, tariffs: list[documents.Tariff]):
        super().__init__(row_width=1)

        for tariff in tariffs:
            button = self.TARIFF.format(title=tariff.title, tariff_id=tariff.id)
            self.insert(button)
