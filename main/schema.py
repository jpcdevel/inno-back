import graphene

from main.gql.gallery.queries import GalleryQueries
from main.gql.tracker.queries import TrackerQueries

from main.gql.gallery.mutations import GalleryMutations
from main.gql.tracker.mutations import TrackerMutations

class Query(GalleryQueries, TrackerQueries):
    pass


class Mutation(GalleryMutations, TrackerMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)