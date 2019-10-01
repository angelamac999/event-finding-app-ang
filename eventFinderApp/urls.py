from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'eventFinderApp'



urlpatterns = [

    # event-finder/

    path('', views.IndexView.as_view(), name='index'),

    # event-finder/1

    path('<int:pk>/', views.EventView.as_view(), name='event'),

    # event-finder/my-account

    path('my-account/', views.AccountView.as_view(), name='account'),

    # event-finder/add-event

    path('addevent/', views.addevent, name='addevent'),

    # event-finder/user

    path("event/edit/", views.edit_event, name="edit_event"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)