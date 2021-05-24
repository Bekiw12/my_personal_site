from django.contrib import admin
from .models import User, Skills, About, Accomplishments

admin.site.register(User)
admin.site.register(Skills)
admin.site.register(About)
admin.site.register(Accomplishments)