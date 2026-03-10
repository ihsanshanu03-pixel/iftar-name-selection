from django.db import models

class Iftar(models.Model):
    person_name = models.CharField(max_length=100)
    iftar_name = models.CharField(max_length=100)

    def __str__(self):
        return self.person_name