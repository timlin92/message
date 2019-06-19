from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', MessageList.as_view()),
    path('<int:pk>/', MessageDetail.as_view()),
    path('create/', MessageCreate.as_view()),
    path('<int:pk>/delete/', MessageDelete.as_view()),
]
