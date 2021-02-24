from django.contrib import admin
from django.urls import path
from crud import views as crud_views
from django.conf import settings
from django.conf.urls.static import static

# Calling function according to paths 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud_views.home, name='home'),
    path('view', crud_views.home, name='home'),
    path('create', crud_views.create, name='create'),
    path('update/<id>', crud_views.update, name='update'),
    path('delete/<id>', crud_views.delete, name='delete'),
    path('login', crud_views.login, name='login'),
    path('register', crud_views.register, name='register'),
    path('logout', crud_views.logout, name='logout'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)   # Serving static data

# Update admin panel header and title 
admin.site.site_header = "XYZ Solution"
admin.site.site_title = "XYZ Solution Admin Portal"
admin.site.index_title = "Welcome to XYZ Solution Researcher Portal"
