from django.db import models

class User(models.Model):
    image = models.ImageField(upload_to='pictures', blank=True)
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    skills = models.ManyToManyField('Skills')

    class Meta():
        verbose_name_plural = "Users"
        verbose_name = "User"

    def __str__(self):
        return self.name


class Skills(models.Model):
    skill = models.CharField(max_length=200)
    class_name = models.CharField(max_length=100, blank=True)

    class Meta():
        verbose_name_plural = "Skills"
        verbose_name = "Skill"

    def __str__(self):
        return self.skill


class About(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    text = models.TextField(max_length=5000)

    class Meta():
        verbose_name_plural = "About"
        verbose_name = "About"

    def __str__(self):
        return self.title


class Accomplishments(models.Model):
    image = models.ImageField(upload_to='pictures', blank=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)

    class Meta():
        verbose_name_plural = "Accomplishments"
        verbose_name = "Accomplishment"

    def __str__(self):
        return self.title



