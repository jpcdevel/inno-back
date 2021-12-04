from django.db import models
from django.contrib.auth.models import AbstractUser

class ExtendedUser(AbstractUser):
    email = models.EmailField(blank=False, unique=True, max_length=255, verbose_name='User Email')
    type = models.CharField(max_length=10)
    startups = models.ManyToManyField("Startup", related_name="user_startups", blank=True)
    # for orgs:
    org_name = models.CharField(max_length=200, default="", blank=True)
    org_descr = models.TextField(default="", blank=True)
    contact_fio = models.CharField(max_length=100, default="", blank=True)
    contact_position = models.CharField(max_length=100, default="", blank=True) # Должность
    contact_phone = models.CharField(max_length=20, default="", blank=True)
    contact_tg = models.CharField(max_length=100, default="", blank=True)
    contact_email = models.EmailField(blank=True, default="")
    contact_skype = models.CharField(max_length=100, default="", blank=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

class Startup(models.Model):
    user = models.ForeignKey(ExtendedUser, null=True, on_delete=models.CASCADE, related_name="startup_user", blank=True)
    tracker = models.ForeignKey(ExtendedUser, null=True, on_delete=models.CASCADE, related_name="startup_tracker", blank=True)
    name = models.CharField(max_length=100, blank=True) # startup name(team name)
    product_name = models.CharField(max_length=100, blank=True) # startup name(team name)
    category = models.ForeignKey("Category", null=True, on_delete=models.DO_NOTHING, related_name="startup_category", blank=True)
    website_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    stage = models.CharField(max_length=20, blank=True) # idea, product, proto
    inculcation_cases = models.TextField(blank=True)
    pilot_thoughts = models.TextField(blank=True)
    team_descr = models.TextField(blank=True)
    product_benefit = models.TextField(blank=True)
    contact_fio = models.CharField(max_length=100, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_tg = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_skype = models.CharField(max_length=100, blank=True)
    pilot = models.CharField(max_length=30, blank=True)
    team_number = models.IntegerField(default=0, blank=True)
    type = models.CharField(max_length=10, blank=True)
    is_strong = models.BooleanField(blank=True, null=True)
    scaling = models.IntegerField(default=0, blank=True)
    problem = models.IntegerField(default=0, blank=True)
    solution = models.IntegerField(default=0, blank=True)
    inculcation = models.IntegerField(default=0)
    ip = models.IntegerField(default=0) # Intelectual property
    presentation = models.ForeignKey("File", null=True, on_delete=models.DO_NOTHING, related_name="startup_presentation", blank=True)
    application = models.ForeignKey("File", null=True, on_delete=models.DO_NOTHING, related_name="startup_application", blank=True) # Заявка на акселератор
    pilots = models.ManyToManyField("Pilot", related_name="startup_pilots", blank=True)
    pending_pilots = models.ManyToManyField("Pilot", related_name="startup_pending_pilots", blank=True)
    inn = models.CharField(max_length=20, blank=True)
    ur_name = models.CharField(max_length=100, blank=True)
    is_approved = models.BooleanField(default=False, blank=True)
    is_min = models.BooleanField(default=False, blank=True)
    comment = models.ForeignKey("Comment", null=True, on_delete=models.DO_NOTHING, related_name="startup_comment", blank=True)

    class Meta:
        ordering = ['-id']

    # File and Pilot models
class File(models.Model):
    name = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)

class Pilot(models.Model):
    org = models.ForeignKey(ExtendedUser, null=True, on_delete=models.CASCADE, related_name="pilot_org", blank=True)
    status = models.IntegerField(default=0)

class Comment(models.Model):
    heading = models.CharField(max_length=100, blank=True)
    text = models.TextField()

class Category(models.Model):
    is_parent = models.BooleanField(blank=True)
    name = models.CharField(max_length=100, blank=True)
    children_cats = models.ManyToManyField('self', related_name='children_categories', symmetrical=False, blank=True)

