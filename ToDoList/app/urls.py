from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('cross_of/<int:id>', views.cross_of, name='cross_off'),
    path('uncross/<int:id>', views.uncross, name='uncross'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('add/', views.PostAddView.as_view(), name='add'),
]
