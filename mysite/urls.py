from django.contrib import admin
from django.urls import path, include  # <-- include is needed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # <-- blog handles root URLs
]
