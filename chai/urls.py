
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.all_chai,name='all_chai'),
    path('<int:chai_id>',views.chai_details,name='chai_details'),
]