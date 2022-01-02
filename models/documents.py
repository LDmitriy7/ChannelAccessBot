import mongoengine as me


class Text(me.Document):
    key = me.StringField(primary_key=True)
    value = me.StringField()

    meta = {
        'allow_inheritance': True,
    }


class WelcomeText(Text):
    key = me.StringField(primary_key=True, default='welcome')


class Tariff(me.Document):
    name = me.StringField(primary_key=True)
    description = me.StringField()
    price = me.IntField()
