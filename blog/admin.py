from django.contrib import admin
from .models import BlogUser, Skills, About, Accomplishments

admin.site.register(BlogUser)
admin.site.register(Skills)
admin.site.register(About)
admin.site.register(Accomplishments)