from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import AbstractUser
from .models import CustomUser
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage



class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/eventFinderApp/account.html')
        else:
            form = CustomUserCreationForm()

            args = {'form': form} 
            return render(request, 'registration/register.html', args)   


def view_profile(request):
    args = {'user' : request.user}
    return render(request, 'eventFinderApp/account.html', args)

# def upload(request):
#     context = {}
#     if request.method == 'POST':
#         #Get the posted form
#         uploaded_file = request.FILES('document')
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         context['url'] = fs.url(name)
#     return render(request, 'upload.html', context)

def upload_pic(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # return redirect('eventFinderApp/account.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'upload.pic.html', locals)




def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return render(request, 'eventFinderApp/event.html',)

    else:
            form = EditProfileForm(instance=request.user)

            args = {'form' : form}
            return render(request, 'users/edit_profile.html', args)



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'users/password_reset.html')

        else:
            return render(request, 'users/change_password.html')
	
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form' : form}
        return render(request, 'users/password.html', args)
    







# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect('/users/change_password')

#         else:
#             return redirect('/users/change_password')
	
#     else:
#         form = PasswordChangeForm(user=request.user)

#         args = {'form' : form}
#         return render(request, 'users/change_password.html', args)
    










# def edit_profile(request):
#     	if request.method == 'POST':
# 		form = UserChangeForm(request.POST, instance=request.user)
# 		if form.is_valid():
# 			form.save() 
# 			return redirect('users/edit_profile.html')
            
# 	else:
# 		form = UserChangeForm(instance=request.user)
# 		args = {'form' : form}
# 		return render(request, 'users/edit_profile.html', args)


# def change_password(request):
#     template_response = views.password_change(request)
#     # Do something with `template_response`
#     return template_response



# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('change_password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'users/change_password.html', {
#         'form': form
#     })



# # @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#         # profile_form = CustomUser(request.POST, request.FILES, instance=request.user.userprofile)  # request.FILES is show the selected image or file
#         # if form.is_valid() and profile_form.is_valid():

#         if form.is_valid():
#             user_form = form.save()
#             custom_form = CustomUserCreationForm.save(False)
#             custom_form.user = user_form
#             custom_form.save()
#             return redirect('accounts:view_profile')
#     else:
#         form = EditProfileForm(instance=request.user)
#         # profile_form = CustomUserCreationForm(instance=request.user.userprofile)
#         args = {}
#         # args.update(csrf(request))
#         args['form'] = form
#         # args['CustomUserCreation_form'] = profile_form
#         return render(request, 'users/edit_profile.html', args)