from django.shortcuts import render
from django.views.generic import TemplateView


class RoomView(TemplateView):
    template_name = "chat/room.html"
