from django.conf.urls import url
from .views import AuthRegister, AuthLogin, AdminRegister, ProfileView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
	url(r'^register/$', AuthRegister.as_view()),
	url(r'^login/$', AuthLogin.as_view()),
	url(r'^addadmin/$', AdminRegister.as_view()),
	url(r'^profile/$', ProfileView.as_view()),

]
