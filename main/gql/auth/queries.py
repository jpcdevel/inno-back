import graphene

from main.gql.types import UserType
from main.models import ExtendedUser

class AuthQueries(graphene.ObjectType):
    get_user_info = graphene.Field(UserType, username=graphene.String(required=True))


    def resolve_get_user_info(root, info, username):
        return ExtendedUser.objects.get(username=username)