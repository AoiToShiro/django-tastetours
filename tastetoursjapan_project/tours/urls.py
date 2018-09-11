from django.conf.urls import url
from tours import views

# Template urls
app_name = 'tours'

urlpatterns = [
    url(r'^$',views.tours, name='tours'),
    url(r'^edooutpost/$',views.edooutpost, name='edooutpost'),
    url(r'^sumofireizakaya/$',views.sumofireizakaya, name='sumofireizakaya'),
]
