from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('comments/', include('comments.urls')),
    path('', RedirectView.as_view(url='comments/')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
