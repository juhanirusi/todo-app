from django.contrib import admin

from .models import Tehtava

class TehtavaAdmin(admin.ModelAdmin):
    fields = ["otsikko", "muistiinpano", "tehty"]

admin.site.register(Tehtava, TehtavaAdmin)