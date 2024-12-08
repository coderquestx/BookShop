from api.models import CategoryResource, CourseResource
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name='v1')
api.register(CategoryResource())
api.register(CourseResource())

urlpatterns = [
    path('', include(api.urls), name='index')
]
