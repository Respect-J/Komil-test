from django.db import models


class Type(models.IntegerChoices):
    UNKNOWN = 0
    STUDENT = 1
    PARENT = 2
    PUPIL = 3
    JOB_SEEKER = 4


class Language(models.IntegerChoices):
    UNKNOWN = 0
    UZ = 1
    RU = 2


class Basemodel(models.Model):
    id = models.CharField(unique=True, max_length=256, primary_key=True)
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)


class Users(Basemodel):
    firtsname = models.CharField(max_length=256)
    language = models.IntegerField(choices=Language.choices, default=Language.UNKNOWN)
    type = models.IntegerField(choices=Type.choices, default=Type.UNKNOWN)
    phone_number = models.CharField(max_length=256)




