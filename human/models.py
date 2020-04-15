from django.db import models


class Human(models.Model):
    GENDER = (
        ("M", "Мужской"),
        ("F", "Женский")
    )
    avatar = models.ImageField("Аватар", null=True, blank=True)
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Фамилия", max_length=50)
    age = models.PositiveSmallIntegerField("Возвраст")
    gender = models.CharField("Пол", max_length=1, choices=GENDER)

    class Meta:
        verbose_name = "Human"
        verbose_name_plural = "Humans"
