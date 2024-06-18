from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Paciente, Familiar, Medico, Medicamento, NotaObservacao, Consulta
from .forms import ConsultaForm, PacienteForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirecionar para a página inicial ou outra página após o login bem-sucedido
            return redirect('index')
        else:
            # Exibir mensagem de erro se as credenciais estiverem incorretas
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    else:
        return render(request, 'login.html')

def index(request):
    pacientes = Paciente.objects.all()
    consultas = Consulta.objects.all()
    medicamentos = Medicamento.objects.all()
    notas = NotaObservacao.objects.all()
    return render(request, 'index.html', {
        'pacientes': pacientes,
        'consultas': consultas,
        'medicamentos': medicamentos,
        'notas': notas
    })

def calendario(request):
    consultas = Consulta.objects.all()
    return render(request, 'calendario.html', {'consultas': consultas})

class PacienteListView(ListView):
    model = Paciente
    template_name = 'pacientes/paciente_list.html'

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'pacientes/paciente_detail.html'

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'pacientes/paciente_confirm_delete.html'
    success_url = reverse_lazy('paciente_list')

# Familiar Views
class FamiliarListView(ListView):
    model = Familiar
    template_name = 'familiares/familiar_list.html'  # Atualizado para usar o template correto

class FamiliarDetailView(DetailView):
    model = Familiar
    template_name = 'familiares/familiar_detail.html'  # Atualizado para usar o template correto

class FamiliarCreateView(CreateView):
    model = Familiar
    fields = ['nome', 'relacao_com_paciente', 'informacoes_contato']
    template_name = 'familiares/familiar_form.html'  # Atualizado para usar o template correto
    success_url = reverse_lazy('familiar_list')

class FamiliarUpdateView(UpdateView):
    model = Familiar
    fields = ['nome', 'relacao_com_paciente', 'informacoes_contato']
    template_name = 'familiares/familiar_form.html'  # Atualizado para usar o template correto
    success_url = reverse_lazy('familiar_list')

class FamiliarDeleteView(DeleteView):
    model = Familiar
    template_name = 'familiares/familiar_confirm_delete.html'  # Atualizado para usar o template correto
    success_url = reverse_lazy('familiar_list')

# Medico Views
class MedicoListView(ListView):
    model = Medico
    template_name = 'medicos/medico_list.html'  # Atualizado para usar o template correto

class MedicoDetailView(DetailView):
    model = Medico
    template_name = 'medicos/medico_detail.html'  # Atualizado para usar o template correto

class MedicoCreateView(CreateView):
    model = Medico
    fields = ['nome', 'especialidade', 'informacoes_contato']
    template_name = 'medicos/medico_form.html'  # Atualizado para usar o template correto
    success_url = reverse_lazy('medico_list')

class MedicoUpdateView(UpdateView):
    model = Medico
    fields = ['nome', 'especialidade', 'informacoes_contato']
    template_name = 'medicos/medico_form.html'  # Atualizado para usar o template correto
    success_url = reverse_lazy('medico_list')

class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'medicos/medico_confirm_delete.html'  # Atualizado para usar o template correto
    success_url = reverse_lazy('medico_list')

# Medicamento Views
class MedicamentoListView(ListView):
    model = Medicamento
    template_name = 'medicamentos/medicamento_list.html'  # Atualizado para usar o template correto

class MedicamentoDetailView(DetailView):
    model = Medicamento
    template_name = 'medicamentos/medicamento_detail.html'  # Atualizado para usar o template correto

class MedicamentoCreateView(CreateView):
    model = Medicamento
    fields = ['nome', 'dosagem', 'frequencia', 'paciente']
    template_name = 'medicamentos/medicamento_form.html'  # Atualizado para usar o template correto
    success_url = reverse_lazy('medicamento_list')

class MedicamentoUpdateView(UpdateView):
    model = Medicamento
    fields = ['nome', 'dosagem', 'frequencia', 'paciente']
    template_name = 'medicamentos/medicamento_form.html'  # Atualizado para usar o template correto
    success_url = reverse_lazy('medicamento_list')

class MedicamentoDeleteView(DeleteView):
    model = Medicamento
    template_name = 'medicamentos/medicamento_confirm_delete.html'  # Atualizado para usar o template correto
    success_url = reverse_lazy('medicamento_list')

# NotaObservacao Views
class NotaObservacaoListView(ListView):
    model = NotaObservacao
    template_name = 'notas/nota_list.html'  # Atualizado para usar o template correto

class NotaObservacaoDetailView(DetailView):
    model = NotaObservacao
    template_name = 'notas/nota_detail.html'  # Atualizado para usar o template correto

class NotaObservacaoCreateView(CreateView):
    model = NotaObservacao
    fields = ['conteudo', 'paciente']
    template_name = 'notas/nota_form.html'  # Atualizado para usar o template correto
    success_url = reverse_lazy('nota_list')

class NotaObservacaoUpdateView(UpdateView):
    model = NotaObservacao
    fields = ['conteudo', 'paciente']
    template_name = 'notas/nota_form.html'  # Atualizado para usar o template correto
    success_url = reverse_lazy('nota_list')

class NotaObservacaoDeleteView(DeleteView):
    model = NotaObservacao
    template_name = 'notas/nota_confirm_delete.html'  # Atualizado para usar o template correto
    success_url = reverse_lazy('nota_list')

# Consulta Views
class ConsultaListView(ListView):
    model = Consulta
    template_name = 'consultas/consulta_list.html'

class ConsultaDetailView(DetailView):
    model = Consulta
    template_name = 'consultas/consulta_detail.html'

class ConsultaCreateView(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consultas/consulta_form.html'
    success_url = reverse_lazy('consulta_list')

class ConsultaUpdateView(UpdateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consultas/consulta_form.html'
    success_url = reverse_lazy('consulta_list')

class ConsultaDeleteView(DeleteView):
    model = Consulta
    template_name = 'consultas/consulta_confirm_delete.html'
    success_url = reverse_lazy('consulta_list')