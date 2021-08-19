from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('blog/', include('blog.urls')),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)