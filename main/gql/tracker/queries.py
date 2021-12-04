import graphene

from main.models import Category, Startup
from main.gql.types import CategoryType, StartupType

class TrackerQueries(graphene.ObjectType):
    get_all_cats = graphene.List(CategoryType)
    get_startup_by_id = graphene.Field(StartupType, id=graphene.ID(required=True))

    def resolve_get_all_cats(root, info):
        return Category.objects.filter(is_parent=False)

    def resolve_get_startup_by_id(root, info, id):
        return Startup.objects.get(id=id)