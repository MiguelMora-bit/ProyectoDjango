from django.db import models

# Create your models here.
class Paciente(models.Model):

    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = ("Paciente")
        verbose_name_plural = ("Pacientes")

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Paciente_detail", kwargs = {"pk": self.pk})

class Tejido(models.Model):

    temperatura = models.FloatField()
    color = models.FloatField()
    inflammation = models.FloatField(verbose_name="Inflamación")
    name = models.ForeignKey(Paciente, on_delete= models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = ("Tejido")
        verbose_name_plural = ("Tejidos")

    def __str__(self):
        return str(self.temperatura)

    def get_absolute_url(self):
        return reverse("Tejido_detail", kwargs = {"pk": self.pk})


