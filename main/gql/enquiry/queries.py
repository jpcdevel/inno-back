import graphene

from main.gql.types import EnquiryType
from main.models import Enquiry


class EnquiryQueries(graphene.ObjectType):

    get_enquiries = graphene.List(EnquiryType)


    def resolve_get_enquiries(root, info, **kwargs):
        r = Enquiry.objects.all()
        return r
