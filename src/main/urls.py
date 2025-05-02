
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from allauth.account.views import LoginView, SignupView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
class CustomSignupView(SignupView):
    template_name = 'account/signup.html'



account_patterns = [
    path("login/", CustomLoginView.as_view(), name="account_login"),
    path("signup/", CustomSignupView.as_view(), name="account_signup"),
    
    

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nippo/', include('nippo.urls')),
    path('accounts/', include('allauth.urls')),
    path("profile/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)