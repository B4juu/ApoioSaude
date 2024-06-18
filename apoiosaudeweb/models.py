from django.db import models
from django.utils.translation import gettext as _
from datetime import date
from datetime import datetime

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    tipo_sanguineo = models.CharField(max_length=10)
    doenca = models.CharField(max_length=200)
    outros_dados = models.TextField()
    foto_perfil = models.ImageField(upload_to='perfil_pics', blank=True, null=True)

    def calcular_idade(self):
        if self.data_nascimento is None:
            return None
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))

    def __str__(self):
        return self.nome

class Familiar(models.Model):
    nome = models.CharField(max_length=100)
    relacao_com_paciente = models.CharField(max_length=100)  # Ex: Pai, Mãe, Cuidador
    informacoes_contato = models.CharField(max_length=200, blank=True, null=True)
    tipo = models.CharField(max_length=50, choices=[('familiar', 'Familiar'), ('cuidador', 'Cuidador')])
    pacientes = models.ManyToManyField('Paciente', related_name='familiares')

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    informacoes_contato = models.CharField(max_length=200)
    pacientes = models.ManyToManyField('Paciente', related_name='medicos')

class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    dosagem = models.CharField(max_length=50)
    frequencia = models.CharField(max_length=50)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
class NotaObservacao(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    conteudo = models.TextField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class Consulta(models.Model):
    data = models.DateField(_('data'))
    hora = models.TimeField(_('hora'))
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    descricao = models.TextField(default='Descrição não fornecida')

    def __str__(self):
        return f"{self.data} {self.hora} - {self.paciente} com {self.medico}"
    
    def formatted_datetime(self):
        # Combine date and time into a datetime object
        combined_datetime = datetime.combine(self.data, self.hora)
        return combined_datetime.strftime('%Y-%m-%dT%H:%M:%S')