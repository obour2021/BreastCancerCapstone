from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.PredictCreate, name='home'),
    path('predictionlist/', views.PredictionList.as_view(), name='dashboard'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('account/', include("django.contrib.auth.urls"))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
