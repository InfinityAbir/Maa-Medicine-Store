from django.contrib import admin
from django.urls import path, include
from pharma import views as pharma_views  # ✅ Import views properly

urlpatterns = [
    path('admin/', admin.site.urls),            # Django admin
    path('pharma/', include('pharma.urls')),    # Pharma app URLs
    path('', pharma_views.home, name='index'),  # Root home
    path('accounts/', include('accounts.urls')) # Login/logout URLs
]
