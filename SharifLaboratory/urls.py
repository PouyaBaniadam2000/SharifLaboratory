from SharifLaboratory import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('weblog/', include('weblog.urls')),
    path('project/', include('project.urls')),
    path('tiding/', include('tiding.urls')),
    path('account/', include('account.urls')),
    path('contact-us/', include('contactus.urls')),
    path('admission/', include('admission.urls')),
]

urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
