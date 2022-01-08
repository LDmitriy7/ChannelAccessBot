from aiogram import types

import keyboards as kb
import texts
from loader import dp
from models import documents


@dp.callback_query_handler(button=kb.Tariffs.TARIFF)
async def show_tariff(query: types.CallbackQuery, button: dict):
    tariff_id: str = button['tariff_id']

    tariff: documents.Tariff = documents.Tariff.objects(id=tariff_id).first()

    if not tariff:
        await query.message.answer('Такого тарифа не существует')
        return

    text = texts.tariff_info.format(
        title=tariff.title,
        price=tariff.price,
        duration=f'{tariff.duration} сек.' if tariff.duration else 'бессрочно',
        description=tariff.description,
    )
    await query.message.answer(text)
