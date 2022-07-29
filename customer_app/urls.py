from django.urls import path

from customer_services_project import settings     
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('services', login_required(views.ServiceList.as_view()) , name = 'service_list'),
    path('service/details/<int:pk>', login_required(views.ServiceDetail.as_view()) , name = 'service details'),
    path('create/new_customer', login_required(views.AddCustomerView.as_view()) , name = 'add_customer_page'),
    path('myProfile/<int:pk>', login_required(views.MyProfilePage.as_view()) , name='My profile page'),
    path('addSevriceCustomer/<service_id>', views.addCsutomerToService , name='add Csutomer To Service'),
    path('removeService/<service_id>/<customer_id>', views.removeCsutomerToService),
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('allCustomers', login_required(views.CustomerList.as_view()) , name = 'all_customers'),
    path('deleteCustomer/<int:pk>', views.CustomerDelete.as_view() , name = 'delete_customer'),
]