from django.contrib import admin

# Register your models here.

from .models import Fish, Insect, SeaCreature

class FishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'season_start', 'season_end', 'location')

class InsectAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'season_start', 'season_end', 'location')

class SeaCreatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'season_start', 'season_end')


admin.site.register(Fish, FishAdmin)
admin.site.register(Insect, InsectAdmin)
admin.site.register(SeaCreature, SeaCreatureAdmin)