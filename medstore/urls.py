<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from pharma import views as pharma_views

urlpatterns = [
    path('admin/', admin.site.urls),            # Django admin
    path('pharma/', include('pharma.urls')),    # Pharma app URLs
    path('', pharma_views.home, name='index'),  # Root redirects to home or login
    path('accounts/', include('accounts.urls')) # Login/logout URLs
=======
"""medstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from pharma import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pharma/', include('pharma.urls')),
    path('', views.home, name='index'),  # Home page
>>>>>>> 840a6ab953452f08603e5f79b0fdbb2fa9ade5bd
]
