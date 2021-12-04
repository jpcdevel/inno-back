import graphene

from main.models import ExtendedUser, Startup, Comment, Pilot

class ChangeProjectStatus(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        username = graphene.String(required=True)
        is_approve = graphene.Boolean(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id, username, is_approve):
        startup = Startup.objects.get(id=id)
        user = ExtendedUser.objects.get(username=username)

        if is_approve:
            startup.tracker = user
            user.startups.add(startup)
            startup.is_approved = True
        else:
            startup.is_min = False

        startup.save()
        user.save()

        return ChangeProjectStatus(ok=True)

class SaveAssessment(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        heading = graphene.String(required=True)
        text = graphene.String(required=True)
        scaling = graphene.Int(required=True)
        ip = graphene.Int(required=True)
        inculcation = graphene.Int(required=True)
        problem = graphene.Int(required=True)
        solution = graphene.Int(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, heading, text, scaling, ip, inculcation, problem, solution, id):
        startup = Startup.objects.get(id=id)

        startup.scaling = scaling
        startup.ip = ip
        startup.inculcation = inculcation
        startup.problem = problem
        startup.solution = solution

        if startup.comment:
            startup.comment.heading = heading
            startup.comment.text = text

        else:
            comment = Comment.objects.create(heading=heading, text=text)
            startup.comment = comment

        startup.save()

        return SaveAssessment(ok=True)

class RequestPilot(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        username = graphene.String(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id, username):
        org = ExtendedUser.objects.get(username=username)
        pilot = Pilot.objects.create(org=org)

        startup = Startup.objects.get(id=id)
        startup.pending_pilots.add(pilot)
        startup.save()

        return RequestPilot(ok=True)

class PilotReply(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        ids = graphene.ID(required=True)
        action = graphene.Boolean(required=True)


    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id, ids, action):
        pilot = Pilot.objects.get(id=id)
        startup = Startup.objects.get(id=ids)

        startup.pending_pilots.remove(pilot)
        if action:
            startup.pilots.add(pilot)

        return PilotReply(ok=True)

class GalleryMutations(graphene.ObjectType):
    change_project_status = ChangeProjectStatus.Field()
    save_assessment = SaveAssessment.Field()
    request_pilot = RequestPilot.Field()
    pilotReply = PilotReply.Field()