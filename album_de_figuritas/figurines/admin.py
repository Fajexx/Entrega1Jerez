from django.contrib import admin

from figurines.models import Player, NationalTeam, Stadium #dejo espacio para separar los import de terceros de los mios

admin.site.register(Player)
admin.site.register(NationalTeam)
admin.site.register(Stadium)
