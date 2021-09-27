from django.db import models

class Tehtava(models.Model):

    otsikko = models.CharField(max_length=200)
    muistiinpano = models.TextField(max_length=20000)
    valmis = models.BooleanField(default=False)

    def __str__(self):
        return self.otsikko