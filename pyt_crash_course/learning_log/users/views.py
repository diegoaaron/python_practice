from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

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