from django.urls import path
from .views import GetCreateSensor, UpdateSensor, CreateMeasurement

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', GetCreateSensor.as_view()),
    path('sensors/<pk>/', UpdateSensor.as_view()),
    path('measurements/', CreateMeasurement.as_view()),
]
