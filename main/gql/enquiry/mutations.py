from django.utils import timezone
import graphene

from main.models import Enquiry


class RegistryEnquiry(graphene.Mutation):
    class Arguments:
        description = graphene.String()
        occurrence = graphene.String()

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, description, occurrence):
        enquiry = Enquiry(description=description,
                          occurrence=occurrence,
                          expiration_date=timezone.now())
        enquiry.save()
        return RegistryEnquiry(ok=True)


class EnquiryMutations(graphene.ObjectType):
    registry_enquiry = RegistryEnquiry.Field()
