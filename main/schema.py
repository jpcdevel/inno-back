import graphene

from main.gql.gallery.queries import GalleryQueries
from main.gql.tracker.queries import TrackerQueries

from main.gql.gallery.mutations import GalleryMutations
from main.gql.tracker.mutations import TrackerMutations

from main.gql.auth.queries import AuthQueries
from main.gql.auth.mutations import AuthMutations

class Query(AuthQueries, GalleryQueries, TrackerQueries):
    pass


class Mutation(AuthMutations, TrackerMutations, GalleryMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)