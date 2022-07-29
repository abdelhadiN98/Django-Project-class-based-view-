from asyncio.windows_events import NULL
import imp
from multiprocessing import context
from turtle import title
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from flask import request
# from customer_app.Repositories.ServiceRepository.service_repository import ServiceRepository

from login_app.models import Employee , Customer , Service
from django.views.generic import ListView , DeleteView , CreateView , UpdateView , DetailView
from django.views.generic.edit import FormView
from django.contrib.auth import logout


# class to render the welcome page and all services added by admin

class ServiceList(ListView):
    model = Service
    template_name = 'welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['this_employee'] = Employee.objects.get(id =self.request.session['employee_id'])
        return context

# class to show the service details page
class ServiceDetail(DetailView):
    model = Service
    template_name = 'serviceDetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['all_customers'] = Customer.objects.all()
        context ['this_employee'] = Employee.objects.get(id =self.request.session['employee_id'])
        return context


    # method to add this customer to this service

def addCsutomerToService(request , service_id):
    this_service = Service.objects.get(id = service_id)
    this_customer = request.POST['customer']
    this_service.customers_have_servives.add(this_customer)
    return redirect(f'/service/details/{service_id}')

    # method to delete this service from this customer
def removeCsutomerToService(request , service_id , customer_id):
    this_service = Service.objects.get(id = service_id)
    this_customer = Customer.objects.get(id = customer_id)
    this_service.customers_have_servives.remove(this_customer)
    return redirect(f'/service/details/{service_id}')

# class to show my profile page and allow to update my information as an employee
class MyProfilePage(UpdateView):
    model = Employee
    fields = ['first_name','last_name','email']
    template_name = 'myProfile.html'
    success_url="/services"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['this_employee'] = Employee.objects.get(id =self.request.session['employee_id'])
        return context


# class to render the bage contains the form to add a new customer 
class AddCustomerView(CreateView):
    model = Customer
    fields = ['first_name','last_name','email']
    template_name = 'customer_form.html'
    # form_class = AddForm
    success_url = '/services'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.managed_by = Employee.objects.get(id =self.request.session['employee_id'])
        self.object.save()
        # form.save()
        return super(AddCustomerView,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['this_employee'] = Employee.objects.get(id =self.request.session['employee_id'])
        return context

# Class to render the bage which shows all the cutomers in table 
class CustomerList(ListView):
    model = Customer
    template_name = 'allCustomers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['this_employee'] = Employee.objects.get(id =self.request.session['employee_id'])
        return context

# class to delete any customer from the table and delete from database
class CustomerDelete(DeleteView):
    model = Customer
    # success_url = '/services'
    success_url = reverse_lazy('all_customers')
