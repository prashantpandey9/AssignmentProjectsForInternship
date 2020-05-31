from django.urls import path	
from .views import AuthRegister, AuthLogin, AdminRegister, ProfileView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
	path('register', AuthRegister.as_view()),
	path('login/', AuthLogin.as_view()),
	path('addadmin/', AdminRegister.as_view()),
	path('profile/', ProfileView.as_view()),

]