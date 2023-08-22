from django.urls import path

from .views import ProyectoView,ProyectoNew,ProyectoEdit, ProyectoDetalleEdit, ProyectoDetalleDel, ProyectoDel, \
     programa,PndView, PndNew, PndEdit, PndDel, DepartamentoView, DepartamentoNew, DepartamentoEdit, DepartamentoDel, \
     MunicipioView, MunicipioNew, MunicipioEdit, MunicipioDel, \
     PuebloView, PuebloNew, PuebloEdit, PuebloDel, \
     PoblacionView, PoblacionNew, PoblacionEdit, PoblacionDel, \
     ComunidadView, ComunidadNew, ComunidadEdit, ComunidadDel, dashboard, \
    ReporteComunidadExcel, DirectorioView
    
urlpatterns = [

    path('proyectos/', ProyectoView.as_view(), name='proyecto_list'),
    path('proyectos/new', ProyectoNew.as_view(), name='proyecto_new'),
    path('proyectos/edit/<int:pk>', ProyectoEdit.as_view(), name='proyecto_edit'),
    path('proyectos/delete/<int:pk>', ProyectoDel.as_view(), name='proyecto_del'),

    path('programas/edit/<int:programa_id>', programa, name='programas_edit'),
    path('programa/edit/<int:pk>', ProyectoDetalleEdit.as_view(), name='programas_detalle_edit'),
    path('programas/<int:programa_id>/delete/<int:pk>', ProyectoDetalleDel.as_view(), name='programas_del'),

   

    path('prioridades/', PndView.as_view(), name='pnd_list'), 
    path('prioridades/new', PndNew.as_view(), name='pnd_new'), 
    path('prioridades/edit/<int:pk>', PndEdit.as_view(), name='pnd_edit'),
    path('prioridades/delete/<int:pk>', PndDel.as_view(), name='pnd_del'),  

    path('departamentos/', DepartamentoView.as_view(), name='departamento_list'),
    path('departamentos/new', DepartamentoNew.as_view(), name='departamento_new'),
    path('departamentos/edit/<int:pk>', DepartamentoEdit.as_view(), name='departamento_edit'),
    path('departamentos/delete/<int:pk>', DepartamentoDel.as_view(), name='departamento_del'),

    path('municipios/', MunicipioView.as_view(), name='municipio_list'),
    path('municipios/new', MunicipioNew.as_view(), name='municipio_new'),
    path('municipios/edit/<int:pk>', MunicipioEdit.as_view(), name='municipio_edit'),
    path('municipios/delete/<int:pk>', MunicipioDel.as_view(), name='municipio_del'),

    path('pueblos/', PuebloView.as_view(), name='pueblo_list'),
    path('pueblos/new', PuebloNew.as_view(), name='pueblo_new'),
    path('pueblos/edit/<int:pk>', PuebloEdit.as_view(), name='pueblo_edit'),
    path('pueblos/delete/<int:pk>', PuebloDel.as_view(), name='pueblo_del'),
   
    path('poblacion/', PoblacionView.as_view(), name='poblacion_list'),
    path('poblacion/new', PoblacionNew.as_view(), name='poblacion_new'),
    path('poblacion/edit/<int:pk>', PoblacionEdit.as_view(), name='poblacion_edit'),
    path('poblacion/delete/<int:pk>', PoblacionDel.as_view(), name='poblacion_del'),

    
    

    #-----------------------------------------------------------------------------
    path('comunidades/', ComunidadView.as_view(), name='comunidad_list'),
    path('comunidades/new', ComunidadNew.as_view(), name='comunidad_new'),
    path('comunidades/edit/<int:pk>', ComunidadEdit.as_view(), name='comunidad_edit'),
    path('comunidades/delete/<int:pk>', ComunidadDel.as_view(), name='comunidad_del'),
    
    path('directorio/', DirectorioView.as_view(), name='directorio_list'),

    #Exportacion de archivos

    path('comunidad/reporte', ReporteComunidadExcel.as_view(), name='reporete_comunidad'),
    #path('dashboard/', Dashboard.as_view(), name='dashboard'),

    path('dashboard', dashboard, name='dashboard'),


    

]