from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import index, calendario

urlpatterns = [
    path('', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('calendario/', calendario, name='calendario'),

    path('pacientes/', views.PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/<int:pk>/', views.PacienteDetailView.as_view(), name='paciente_detail'),
    path('pacientes/create/', views.PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/<int:pk>/update/', views.PacienteUpdateView.as_view(), name='paciente_update'),
    path('pacientes/<int:pk>/delete/', views.PacienteDeleteView.as_view(), name='paciente_delete'),
    
    path('familiares/', views.FamiliarListView.as_view(), name='familiar_list'),
    path('familiares/<int:pk>/', views.FamiliarDetailView.as_view(), name='familiar_detail'),
    path('familiares/create/', views.FamiliarCreateView.as_view(), name='familiar_create'),
    path('familiares/<int:pk>/update/', views.FamiliarUpdateView.as_view(), name='familiar_update'),
    path('familiares/<int:pk>/delete/', views.FamiliarDeleteView.as_view(), name='familiar_delete'),
    
    path('medicos/', views.MedicoListView.as_view(), name='medico_list'),
    path('medicos/<int:pk>/', views.MedicoDetailView.as_view(), name='medico_detail'),
    path('medicos/create/', views.MedicoCreateView.as_view(), name='medico_create'),
    path('medicos/<int:pk>/update/', views.MedicoUpdateView.as_view(), name='medico_update'),
    path('medicos/<int:pk>/delete/', views.MedicoDeleteView.as_view(), name='medico_delete'),
    
    path('medicamentos/', views.MedicamentoListView.as_view(), name='medicamento_list'),
    path('medicamentos/<int:pk>/', views.MedicamentoDetailView.as_view(), name='medicamento_detail'),
    path('medicamentos/create/', views.MedicamentoCreateView.as_view(), name='medicamento_create'),
    path('medicamentos/<int:pk>/update/', views.MedicamentoUpdateView.as_view(), name='medicamento_update'),
    path('medicamentos/<int:pk>/delete/', views.MedicamentoDeleteView.as_view(), name='medicamento_delete'),
    
    path('notas/', views.NotaObservacaoListView.as_view(), name='nota_list'),
    path('notas/<int:pk>/', views.NotaObservacaoDetailView.as_view(), name='nota_detail'),
    path('notas/create/', views.NotaObservacaoCreateView.as_view(), name='nota_create'),
    path('notas/<int:pk>/update/', views.NotaObservacaoUpdateView.as_view(), name='nota_update'),
    path('notas/<int:pk>/delete/', views.NotaObservacaoDeleteView.as_view(), name='nota_delete'),
    
    path('consultas/', views.ConsultaListView.as_view(), name='consulta_list'),
    path('consultas/<int:pk>/', views.ConsultaDetailView.as_view(), name='consulta_detail'),
    path('consultas/create/', views.ConsultaCreateView.as_view(), name='consulta_create'),
    path('consultas/<int:pk>/update/', views.ConsultaUpdateView.as_view(), name='consulta_update'),
    path('consultas/<int:pk>/delete/', views.ConsultaDeleteView.as_view(), name='consulta_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)