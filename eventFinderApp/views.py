from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import Event, Category
from .forms import EventForm
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):

    template_name = 'eventFinderApp/index.html'

    context_object_name = 'events_list'


    def get_queryset(self):

        '''Return the events.'''

        return Event.objects.all()



class AccountView(generic.ListView):

    template_name = 'eventFinderApp/account.html'

    context_object_name = 'events_list'



    def get_queryset(self):

        '''Return the events.'''

        return Event.objects.filter()



    

class EventView(generic.DetailView):

    model = Event

    template_name = 'eventFinderApp/event.html'



@login_required(login_url = 'login')

def addevent(request):

    # if this is a POST request, we need to process the form data

    if request.method == 'POST':

        # create a form instance and populate it with data from the request

        form = EventForm(request.POST)

        # check whether it is valid

        if form.is_valid():

            #process the data in form.cleaned_data as required

            #get the new event from the form but don't save it yet

            new_event = form.save(commit=False)

            # add the host

            new_event.host = request.user

            form.save()

            return HttpResponseRedirect(reverse('eventFinderApp:index'))

        return render(request, 'eventFinderApp/addevent.html', {'eventform': form})

    # if it is a GET request (or any other method) we'll create a blank form

    else:

        eventform = EventForm()

        return render(request, 'eventFinderApp/addevent.html', {'eventform': eventform})
       



def account(request):

    return render(request, 'eventFinderApp/account.html')





# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse, reverse_lazy
# from django.views import generic
# from django.shortcuts import render
# from .models import Event
# from .forms import NewEventForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login
# from django.contrib.auth import logout
# from django.contrib.auth.models import Permission, User
# # from .forms import NewEventForm, AccountForm

# class IndexView(generic.ListView):
#     template_name = 'eventFinderApp/index.html'
#     context_object_name = 'events_list'

#     def get_queryset(self):
#         '''Return the events.'''
#         return Event.objects.all()

# class EventView(generic.DetailView):
#     model = Event
#     template_name = 'eventFinderApp/event.html'

# class AccountView(generic.DetailView):
#     model = User
#     template_name = 'eventFinderApp/account.html'

# def account(request):
#     accountform = AccountForm()
#     return render(request, 'eventFinderApp/account.html', {'accountform': accountform})

# @login_required(login_url='login')
# def add_event(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NewEventForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             # return HttpResponseRedirect('/thanks/')
#             form.save()
#             return HttpResponseRedirect(reverse('eventFinderApp:index'))

#         return render(request, 'eventFinderApp/newEventForm.html', {'eventform': form})

#     # if a GET (or any other method) we'll create a blank form

#     else:

#         eventform = NewEventForm()

#         return render(request, 'eventFinderApp/newEventForm.html', {'eventform': eventform})


# def logout_user(request):
#     logout(request)
#     form = AccountForm(request.POST or None)
#     context = {
#         "form": form,
#     }
#     return render(request, 'eventFinderApp/account.html', context)


# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 events = Event.objects.filter(user=request.user)
#                 return render(request, 'eventFinderApp/index.html', {'events': events})
#             else:
#                 return render(request, 'eventFinderApp/acccount.html', {'error_message': 'Your account has been disabled'})
#         else:
#             return render(request, 'eventFinderApp/acccount.html', {'error_message': 'Invalid login'})
#     return render(request, 'eventFinderApp/acccount.html')


# def register(request):
#     form = AccountForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user.set_password(password)
#         user.save()
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 events = Event.objects.filter(user=request.user)
#                 return render(request, 'eventFinderApp/acccount.html', {'events': events})
#     context = {
#         "form": form,
#     }
#     return render(request, 'eventFinderApp/acccount.html', context)


# class NewEventView(generic.CreateView):
#     template_name ='eventFinderApp/event_adder.html'
#     form_class = NewEventForm
#     queryset = Event.objects.all()
#     success_url = '/event-finder/thanks/'

# def get_new_event(request):
#     # if this is a POST request we need to process the form data

#     if request.method == 'POST':

#     # create a form instance and populate it with data from the request:

#         form = NewEventForm(request.POST)

#     # check whether it's valid:

#     if form.is_valid():

#                 # process the data in form.cleaned_data as required

#                 # ...

#                 # redirect to a new URL:

#         return HttpResponseRedirect('/thanks/')



#         # if a GET (or any other method) we'll create a blank form

#     else:

#         form = NewEventForm()



#     return render(request, 'eventFinderApp/event_adder.html', {'form': form})

# def account(request):
    
#     return render(request, 'eventFinderApp/account.html')



# def thanks(request):

#     return render(request, 'eventFinderApp/thanks.html')