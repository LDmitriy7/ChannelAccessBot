from aiogram import types

import api
import keyboards as kb
import texts
from loader import dp, wallet
from models import models


@dp.callback_query_handler(button=kb.Tariffs.TARIFF)
@dp.callback_query_handler(button=kb.PaymentOptions.CANCEL)
async def show_tariff(query: types.CallbackQuery, button: dict):
    tariff_id = int(button['tariff_id'])
    tariff = api.get_tariff(tariff_id)

    if not tariff:
        await query.message.answer('Такого тарифа не существует')
        return

    text = texts.tariff_info.format(
        title=tariff.title,
        price=tariff.price,
        duration=f'{tariff.duration} сек.' if tariff.duration else 'бессрочно',
        description=tariff.description,
    )
    await query.message.edit_text(text, reply_markup=kb.TariffOptions(tariff.id))


@dp.callback_query_handler(button=kb.TariffOptions.BACK)
async def back(query: types.CallbackQuery):
    reply_markup = kb.Tariffs(models.tariffs)
    await query.message.edit_text(texts.ask_to_choose_tariff, reply_markup=reply_markup)


@dp.callback_query_handler(button=kb.TariffOptions.PAY)
async def pay(query: types.CallbackQuery, button: dict):
    tariff_id = int(button['tariff_id'])
    tariff = api.get_tariff(tariff_id)

    if not tariff:
        await query.message.answer('Такого тарифа не существует')
        return

    await query.answer('🗝')
    invoice_url = wallet.get_invoice_url(amount=tariff.price, comment=f'{query.from_user.id}')
    await query.message.edit_text(texts.payment_info, reply_markup=kb.PaymentOptions(invoice_url, tariff_id))
