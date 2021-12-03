import graphene
import graphql_jwt
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError

from main.models import ExtendedUser
from main.gql.types import UserType

class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)

class StartupRegister(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, username, password):
        if len(ExtendedUser.objects.filter(username=username)) == 0:
            user = ExtendedUser.objects.create(username=username)
            user.set_password(password)
            user.email = f"mail{user.id}@mail.mail"
            user.save()
        else:
            raise ValidationError("Such username already exists")
        return StartupRegister(ok=True)

class AuthMutations(graphene.ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revokeToken = graphql_jwt.Revoke.Field()
    startup_register = StartupRegister.Field()