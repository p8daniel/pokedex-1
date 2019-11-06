from peewee import *

from .database import db


class CommonModel(Model):
    class Meta:
        database = db
        schema = 'consommables'


class Potion(CommonModel):
    id = PrimaryKeyField()
    # name = CharField()
    amount = CharField()

    def use(self, pokemon):
        pokemon.heal(self.amount)


class PotionCollection(CommonModel):
    id = PrimaryKeyField()
    amount = CharField()

with db:
    Potion.create_table(fail_silently=True)
    PotionCollection.create_table(fail_silently=True)