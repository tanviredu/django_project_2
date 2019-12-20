from django.contrib import admin
from django.urls import path,include
from . import views
## using the generic view for the rendering
## why this name in the url is used??
## because in the template when we use the 
## url to redirect we use the name
## {% url 'post_detail' %}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Postlist.as_view(),name='home'),
    path('<slug:id>/',views.detail,name='detail'),
]
