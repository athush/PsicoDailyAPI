from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    telefone=models.CharField(max_length=12, blank=True)
    description=models.CharField(max_length=255, blank=True)
    foto = models.ImageField(blank=True, upload_to='users/pictures')
    
    class Meta:
        abstract = True
        

class Psychologist(User):
    crp = models.CharField(max_length=6)
    
    def __str__(self) -> str:
        return f'Psicologo: {self.last_name}'

class Patient(User):
    psicologo = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'Paciente: {self.last_name}'
    
class Record(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    data_hora = models.DateTimeField(auto_now_add=True)
    
    
class Consulta(models.Model):
    psicologo = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    paciente = models.OneToOneField(Patient, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    observacoes = models.CharField(max_length=255, blank=True)