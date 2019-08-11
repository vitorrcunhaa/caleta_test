from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('billing/', include('billing.urls'), name='billing'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
