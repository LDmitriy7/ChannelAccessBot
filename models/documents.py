from typing import Optional

import mongoengine as me
from bson import ObjectId

import texts


class Text(me.Document):
    key = me.StringField(primary_key=True)
    value = me.StringField()

    meta = {
        'allow_inheritance': True,
    }


class WelcomeText(Text):
    key = me.StringField(primary_key=True, default='welcome')


class Tariff(me.Document):
    title: str = me.StringField()
    description: str = me.StringField()
    price: int = me.IntField()
    duration: Optional[int] = me.IntField()
    channel_id: int = me.IntField()


tariff1 = Tariff(
    id=ObjectId('61d9de96fc51338d9868d842'),
    title='🎉 Доступ навсегда',
    description=texts.tariff1_description,
    price=379,
).save()
