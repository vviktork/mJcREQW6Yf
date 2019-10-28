from django.urls import path
from schedule.views import Servis2View, Servis3View

urlpatterns = [
    path(r'^$', Servis2View.as_view()),
    path(r'^$', Servis3View.as_view()),

]