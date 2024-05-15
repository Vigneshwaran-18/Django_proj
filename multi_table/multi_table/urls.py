
from django.contrib import admin
from django.urls import path
from mtable.views import hw,mt
from vc.views import vc_count

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hw),
    path('mtab/<int:n>/<int:m>', mt),
    path('vc/<str:st>',vc_count),
]
