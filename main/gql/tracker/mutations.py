import graphene
from main.models import Startup, Category, ExtendedUser
from main.gql.types import StartupType

class SaveStartupInformation(graphene.Mutation):
    class Arguments:
        startup_id = graphene.ID(required=True)
        team_name = graphene.String(required=True)
        cat = graphene.String(required=True)
        inn = graphene.String(required=True)
        ur_name = graphene.String(required=True)
        team_number = graphene.Int(required=True)
        stage = graphene.String(required=True)
        website_url = graphene.String(required=True)
        brief_description = graphene.String(required=True)
        pilot_thoughts = graphene.String(required=True)
        product_benefit = graphene.String(required=True)
        inculcation_cases = graphene.String(required=True)
        team_descr = graphene.String(required=True)
        fio = graphene.String(required=True)
        phone = graphene.String(required=True)
        email = graphene.String(required=True)
        tg = graphene.String(required=True)
        skype = graphene.String(required=True)
        product_name = graphene.String(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, startup_id, team_name, cat, inn, ur_name, team_number, stage, website_url, brief_description, pilot_thoughts, product_benefit, inculcation_cases, team_descr, fio, phone, email, tg, skype, product_name):
        startup = None
        if len(Startup.objects.filter(id=startup_id)) != 0:
            startup = Startup.objects.get(id=startup_id)
        else:
            startup = Startup.objects.create()

        startup.name = team_name
        startup.category = Category.objects.get(name=cat)
        startup.inn = inn
        startup.ur_name = ur_name
        startup.team_number = team_number
        startup.stage = stage
        startup.website_url = website_url
        startup.description = brief_description
        startup.pilot_thoughts = pilot_thoughts
        startup.product_benefit = product_benefit
        startup.inculcation_cases = inculcation_cases
        startup.team_descr = team_descr
        startup.contact_fio = fio
        startup.contact_phone = phone
        startup.contact_tg = tg
        startup.contact_email = email
        startup.contact_skype = skype
        startup.product_name = product_name

        startup.is_min = True
        startup.save()

        return SaveStartupInformation(ok=True)

class CreateStartup(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
    
    startup = graphene.Field(StartupType)

    @classmethod
    def mutate(cls, root, info, username):
        user = ExtendedUser.objects.get(username=username)
        startup = Startup.objects.create()

        user.startups.add(startup)
        startup.user = user

        user.save()
        startup.save()

        return CreateStartup(startup=startup)

class TrackerMutations(graphene.ObjectType):
    save_startup_information = SaveStartupInformation.Field()
    create_startup = CreateStartup.Field()