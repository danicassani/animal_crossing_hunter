from django.contrib import admin

# Register your models here.

from .models import Fish, Insect, SeaCreature

admin.site.register(Fish)
admin.site.register(Insect)
admin.site.register(SeaCreature)