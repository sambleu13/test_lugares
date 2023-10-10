from django.urls import path
from .views import ListaLugaresView, DetalleLugarView, ListaDireccionesView

urlpartterns = [
    path('lugares/', ListaLugaresView.as_view(), name="lista-lugares"),
    path('lugares/<int:pk>', DetalleLugarView.as_view(), name="detalle-libro"),
    path('lugares/', ListaDireccionesView.as_view(), name="lista-lugares"),

]