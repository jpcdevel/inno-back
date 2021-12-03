from graphene_django import DjangoObjectType

from main.models import ExtendedUser, Enquiry


class UserType(DjangoObjectType):
    class Meta:
        model = ExtendedUser
        fields = (
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "type"
        )


class EnquiryType(DjangoObjectType):
    class Meta:
        model = Enquiry
        fields = ("__all__")