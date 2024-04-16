from django.urls import include, path

from api_v47.views.post_line import PostAPIView

urlpatterns = [
    path('post_line/', PostAPIView.as_view(), name='post_line')
]