from django import forms
from .models import Consulta, Paciente
from django.forms.widgets import DateInput

TIPOS_SANGUINEOS = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

class ConsultaForm(forms.ModelForm):
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Consulta
        fields = ['data', 'hora', 'paciente', 'medico', 'descricao']

class PacienteForm(forms.ModelForm):
    tipo_sanguineo = forms.ChoiceField(
        choices=TIPOS_SANGUINEOS,
        widget=forms.Select
    )
    data_nascimento = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'},
            format='%Y-%m-%d'  # Ajuste o formato aqui conforme o esperado pelo HTML5
        )
    )

    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'tipo_sanguineo', 'doenca', 'outros_dados', 'foto_perfil']
