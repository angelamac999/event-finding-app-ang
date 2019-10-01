from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from rest_framework import routers
from eventFinderApp import viewsets
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
from users import viewsets as UserViewsets

# from django.conf import settings
# from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'events', viewsets.EventViewSet)
router.register(r'users', UserViewsets.CustomUserViewSet)


urlpatterns = [
    path("", include("eventFinderApp.urls")),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r"^admin/", admin.site.urls),
    path("users/", include("django.contrib.auth.urls")),
    path("users/", include("users.urls")),
    path("profile/edit/", include("users.urls")),
    path('api/', include(router.urls)),
    path(r'api-auth-token/', views.obtain_auth_token),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

