from blogzinho import views
from django.urls import path


urlpatterns = [
    path('', views.meu_blog),
    path('teste/', views.teste_foda)
]