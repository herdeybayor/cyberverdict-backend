from django.http import JsonResponse
from django.urls import path

# URLConf
urlpatterns = [
    path(
        "", lambda request: JsonResponse({"message": "Hello, World! :)"}), name="home"
    ),
    path("ping/", lambda request: JsonResponse({"message": "pong!"}), name="ping"),
]
