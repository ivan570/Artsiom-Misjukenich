from django.urls import path
from .views import RoomView

urlpatterns = [
    path("<str:room_name>/", RoomView.as_view(), name="room"),
]
