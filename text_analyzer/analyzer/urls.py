


from django.urls import path
from analyzer import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
	path('', views.analyze, name="analyze_text"),
	path('submit_text', views.get_prediction, name="submit_text"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
