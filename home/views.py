from .utils import add_event , delete_event
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.views.generic.list import ListView
from django.urls import reverse , reverse_lazy
from .models import Event 
from django.views.generic.edit import CreateView , DeleteView


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')



class Event_Create(SuccessMessageMixin,CreateView):
    model = Event
    fields = ['name','starttime','endtime']
    template_name = 'home/create_event.html'
    success_message = 'Your Event is Created'

    def form_valid(self , form):
        form.instance.user = self.request.user
        startime = form.cleaned_data['starttime']
        print(startime)
        endtime = form.cleaned_data['endtime']
        print(endtime)
        name = form.cleaned_data['name']
        print(name)
        a = add_event(startime = startime , endtime = endtime , name = name )
        form.instance.unique_id = a
        return super(Event_Create,self).form_valid(form)

    def get_success_url(self , **kwargs):
        super(Event_Create,self).get_success_url(**kwargs)
        success_url = reverse('event:list')
        return success_url    


class Event_delete(SuccessMessageMixin , DeleteView):
    model = Event
    success_url = reverse_lazy('home')
    success_message = "Event is Delete succesfully"
    template_name = 'home/event_delete.html'


    def get_queryset(self ,**kwargs):
        queryset = super(Event_delete ,self).get_queryset(**kwargs)
        q = Event.objects.get(pk = self.kwargs.get('pk'))
        # print(q.unique_id)
        # delete_event(delete_id = q.unique_id)
        return queryset.filter(pk=self.kwargs.get('pk'))

     

    def post(self, request , *args , **kwargs):
        q = Event.objects.get(pk = self.kwargs.get('pk'))
        print(q.unique_id)
        delete_event(delete_id = q.unique_id)
        return self.delete(request, *args, **kwargs)




class Event_list(ListView):
    model = Event
    template_name = 'home/event_list.html'
