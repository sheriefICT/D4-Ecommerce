from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('settings.urls')),
    path('products/', include('product.urls')),



    path("__debug__/", include("debug_toolbar.urls")),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))




]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)