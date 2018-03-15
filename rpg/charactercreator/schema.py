from graphene_django import DjangoObjectType
import graphene
from .models import Character as CharacterModel
from armory.models import Item as ItemModel
from armory.models import Weapon as WeaponModel

class Item(DjangoObjectType):
    class Meta:
        model = ItemModel

class Weapon(DjangoObjectType):
    class Meta:
        model = WeaponModel

class Character(DjangoObjectType):
    inventory = graphene.List(Item)

    @graphene.resolve_only_args
    def resolve_inventory(self):
        return self.inventory.all()

    class Meta:
        model = CharacterModel

class Query(graphene.ObjectType):
    characters = graphene.List(Character)

    def resolve_characters(self, info):
        return CharacterModel.objects.all()

schema = graphene.Schema(query=Query)
