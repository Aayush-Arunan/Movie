from django.urls import path
from .import views
app_name='movieapp'
urlpatterns = [
    path('',views.index,name='index'),

    path('home',views.home,name='Home'),

    path('movie/<int:movie_id>/',views.detail,name='detail'),

    path('add/',views.add_movie,name='add_movie'),

    path('update/<int:id>/',views.update,name='update'),

    path('delete/<int:id>/', views.delete, name='delete'),

    path('register/',views.Register,name='register'),

    path('login/',views.user_login,name='login'),

    path('logout',views.user_logout,name='logout'),

]
