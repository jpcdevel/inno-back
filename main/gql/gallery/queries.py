import graphene

from main.gql.types import StartupType, CategoryType
from main.models import Startup, Category

class GalleryQueries(graphene.ObjectType):
    get_startups_by_filters = graphene.List(StartupType, stage=graphene.Int(required=True), pilot=graphene.Int(required=True), inculcation=graphene.Int(required=True), teamNumber=graphene.Int(required=True), scaling=graphene.Int(required=True), problems=graphene.Int(required=True), solutions=graphene.Int(required=True))
    get_all_startup_applications = graphene.List(StartupType)
    get_all_superior_cats = graphene.List(CategoryType)

    def resolve_get_startups_by_filters(root, info, stage, pilot, inculcation, teamNumber, scaling, problems, solutions):
        stage_c = None
        team_number_c1 = None
        team_number_c2 = None
        scaling_c = None
        problems_c = None
        solutions_c = None

        res = Startup.objects.filter(is_approved=True)
        if stage != 0:
            if stage == 1:
                stage_c = "Идея"
            if stage == 2:
                stage_c = "Продукт"
            if stage == 3:
                stage_c = "Прототип"

            res = res.filter(stage=stage_c)

        if teamNumber != 0:
            if teamNumber == 1:
                team_number_c1 = 0
                team_number_c2 = 20
            if teamNumber == 2:
                team_number_c1 = 20
                team_number_c2 = 100
            if teamNumber == 3:
                team_number_c1 = 100
                team_number_c2 = 500
            if teamNumber == 4:
                team_number_c1 = 500
                team_number_c2 = 1000

            res = res.filter(team_number__gte=team_number_c1, team_number__lte=team_number_c2)

        if scaling != 0:
            if scaling == 1:
                scaling_c = 3
            if scaling == 3:
                scaling_c = 1

            res = res.filter(scaling=scaling_c)

        if problems != 0:
            if problems == 1:
                problems_c = 3
            if problems == 3:
                problems_c = 1

            res = res.filter(problem=problems_c)

        if solutions != 0:
            if solutions == 1:
                solutions_c = 3
            if solutions == 3:
                solutions_c = 1

            res = res.filter(solution=solutions_c)

        
        

        return res

    def resolve_get_all_startup_applications(root, info):
        return Startup.objects.filter(is_min=True, is_approved=False)
    
    def resolve_get_all_superior_cats(root, info):
        return Category.objects.filter(is_parent=True)