from django.contrib import admin
from django.urls import path, include

# views importadas
from hello_world import views

urlpatterns = [
	path('admin/', admin.site.urls),
	# URL configurada
	# path('', views.index, name="homepage")
	path('', include('pages.urls')),
]
