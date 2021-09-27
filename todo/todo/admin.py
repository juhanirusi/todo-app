from django.contrib import admin

from .models import Tehtava

class TehtavaAdmin(admin.ModelAdmin):
    fields = ["otsikko", "muistiinpano", "valmis"]

admin.site.register(Tehtava, TehtavaAdmin)