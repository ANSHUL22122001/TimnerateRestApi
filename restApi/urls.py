from django.conf.urls import url
from restApi import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('department/',views.departmentApi),
    url('department/([0-9]+)',views.departmentApi),

    # url(r'^employee$',views.employeeApi),
    # url(r'^employee/([0-9]+)$',views.employeeApi),

    # url(r'^employee/savefile',views.SaveFile)
]