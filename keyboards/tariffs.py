from aiogram.types import InlineKeyboardMarkup
from aiogram_utils.keyboards import InlineKeyboardButton

from models import models


class Tariffs(InlineKeyboardMarkup):
    TARIFF = InlineKeyboardButton('{title}', callback_data='tariff:{tariff_id}')

    def __init__(self, tariffs: list[models.Tariff]):
        super().__init__(row_width=1)

        for tariff in tariffs:
            button = self.TARIFF.format(title=tariff.title, tariff_id=tariff.id)
            self.insert(button)


class TariffOptions(InlineKeyboardMarkup):
    PAY = InlineKeyboardButton('💳 ОПЛАТИТЬ', callback_data='pay:{tariff_id}')
    BACK = InlineKeyboardButton('👈 НАЗАД', callback_data='back')

    def __init__(self, tariff_id: int):
        super().__init__(row_width=1)

        self.add(
            self.PAY.format(tariff_id=tariff_id),
            self.BACK,
        )


class PaymentOptions(InlineKeyboardMarkup):
    PAY = InlineKeyboardButton('✅ ПЕРЕЙТИ К ОПЛАТЕ', url='{invoice_url}')
    CHECK_PAYMENT = InlineKeyboardButton('⏳ Я ОПЛАТИЛ', callback_data='check_payment')
    CANCEL = InlineKeyboardButton('🚫 ОТМЕНА', callback_data='cancel:tariff:{tariff_id}')

    def __init__(self, invoice_url: str, tariff_id: int):
        super().__init__(row_width=1)

        self.add(
            self.PAY.format(invoice_url=invoice_url),
            self.CHECK_PAYMENT,
            self.CANCEL.format(tariff_id=tariff_id),
        )
