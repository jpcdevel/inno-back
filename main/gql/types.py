from graphene_django import DjangoObjectType

from main.models import ExtendedUser, Startup, File, Pilot, Comment, Category

class UserType(DjangoObjectType):
    class Meta:
        model = ExtendedUser
        fields = "__all__"

class StartupType(DjangoObjectType):
    class Meta:
        model = Startup
        fields = "__all__"

class FileType(DjangoObjectType):
    class Meta:
        model = File
        fields = "__all__"

class PilotType(DjangoObjectType):
    class Meta:
        model = Pilot
        fields = "__all__"

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = "__all__"

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"