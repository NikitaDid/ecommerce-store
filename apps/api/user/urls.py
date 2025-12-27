from django.urls import path
from apps.api.user.views import LoginView

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view())
]
