from scientific_mission.models import *
from scientific_mission.forms import *
from django.contrib import admin


admin.site.register(Type)


class ScientificMissionAdmin(admin.ModelAdmin):
    fields = ['person', 'amount_paid', 'mission', 'project_activity', 'origin_city', 'destination_city', 'departure',
              'arrival']
    list_display = ('id', 'value', 'person', 'mission', 'destination_city', 'departure', 'arrival')
    list_display_links = ('id',)
    form = ScientificMissionForm
admin.site.register(ScientificMission, ScientificMissionAdmin)
