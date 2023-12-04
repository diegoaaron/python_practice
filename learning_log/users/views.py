from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Usuario o pass invalido')
        return self.render_to_response(self.get_context_data(form=form))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username = new_user.username,
                                              password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)

