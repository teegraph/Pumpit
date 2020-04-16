from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from human.models import Human


class Match(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Фамилия", max_length=50)
    age = models.PositiveSmallIntegerField("Возраст")
    gender = models.CharField("Пол", max_length=1)
    human_id = models.IntegerField("Human")


@receiver(post_save, sender=Human)
def create_match(sender, instance, created, **kwargs):
    if created:
        Match.objects.create(human=instance, first_name=instance.first_name, second_name=instance.second_name,
                             age=instance.age, gender=instance.gender)
