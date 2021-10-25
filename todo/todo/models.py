from django.db import models

#class Kategoria(model.Model):
#    nimi = models.CharField(max_length=100)


class Tehtava(models.Model):

    otsikko = models.CharField(max_length=200)
    muistiinpano = models.TextField(max_length=2000, default="", blank=True)
    tehty = models.BooleanField(default=False)
    #kategoria = models.ForeignKey(Kategoria, one_delete=models.SET_NULL, null=True, blank=True,)

    # CASCADE --> Poistaa myös tehtävät kategorian sisällä.
    # SET_NULL --> Poistaa vain kategorian.

    def __str__(self):
        return self.otsikko