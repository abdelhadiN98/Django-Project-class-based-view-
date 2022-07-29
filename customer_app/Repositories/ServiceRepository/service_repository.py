
# from login_updated_app.models import Employee,Service,Customer
# from django.shortcuts import redirect, render


# class ServiceRepository(object):

#     @staticmethod
#     def get_service_detalits_by_service_id(request , service_id):
#         this_employee = Employee.objects.get(id=request.session['employee_id'])
#         this_service = Service.objects.get(id = service_id)
#         all_customers = Customer.objects.all()
#         this_service_customers = this_service.customers_have_servives.all()
#         context = {
#             'this_service' : this_service,
#             'all_customers' : all_customers,
#             'this_service_customers' : this_service_customers,
#             'this_employee' : this_employee,
#         }
#         return render(request , 'serviceDetails.html' ,context)