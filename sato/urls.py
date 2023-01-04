from django.urls import path
from .views import RoomView,HerView,ContactFormView, SatoCreateView


app_name = "hisroom"

urlpatterns = [
    path('', RoomView.as_view(), name = "room"),
    path('herroom/', HerView.as_view(), name = "herroom"),
    path('contact/',ContactFormView.as_view(), name='contact'),
    path('friends/',SatoCreateView.as_view(), name='realfriends')
]