from django.urls import path
from activity import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name='about'),
    path('register', views.registration, name="register"),
    path("login", views.studlogin, name="login"),
    path('updatepassword',views.updatepassword,name='updatepassword'),
    path('updateinfo',views.updateinfo,name='updateinfo'),
    path('stufeedback/',views.stufeedback,name='stufeedback'),
    path('logout/', views.logout_view, name="logout"),


    path('facultylogin', views.flogin, name="facultylogin"),
    path('facupdatepass/', views.facupdatepass, name='facupdatepass'),
   path('facupdateinfo/', views.facupdateinfo, name='facupdateinfo'),
   path('facufeedback/', views.facufeedback, name='facufeedback'),


#    path('adminlogin', views.alogin, name="adminlogin")
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
