from django.db import models
import uuid


class Basemodel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4()
        super().save(*args, **kwargs)


class Webinars(Basemodel):
    name_uz = models.CharField(max_length=511, blank=True, null=True)
    name_ru = models.CharField(max_length=511, blank=True, null=True)
    description_uz = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="img/", null=True, blank=True)
    date = models.DateTimeField("Webinar date", null=True, blank=True)
