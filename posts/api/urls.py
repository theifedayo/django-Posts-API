from django.urls import path

from .views import PostRUD

app_name = 'posts'

urlpatterns = [
	path('<int:pk>/', PostRUD.as_view(), name='post-rud'),
]