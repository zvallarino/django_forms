from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView
from sato.forms import ContactForm
from sato.models import PeepsHeKnows

# Create your views here.

class RoomView(TemplateView):
    template_name = 'sato/hisroom.html'

class HerView(TemplateView):
    template_name = 'sato/misaki_room.html'

class SatoCreateView(CreateView):
    model = PeepsHeKnows
    fields = "__all__"
    success_url = reverse_lazy('hisroom:herroom')

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'sato/contact.html'

    success_url = reverse_lazy('hisroom:herroom')

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)