from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app.urls")),
    path("anime/id=<int:anime_id>", include("app.urls")),
    path("api-proxy/<str:search_query>", include("app.urls"))
]
