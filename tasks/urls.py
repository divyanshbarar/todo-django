from django.urls import path
from . import views



admin.site.site_header="TODO Page Admin"
admin.site.site_title=" Welcome Divyansh"
admin.site.index_title="This is TODO Page Backend"

urlpatterns = [
    path('',views.index,name="home"),
    path('update/<str:pk>/',views.updateTask,name="update"),
    path('delete/<str:pk>/',views.deleteTask,name="delete")
]
