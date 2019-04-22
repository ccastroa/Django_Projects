from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.template.loader import render_to_string

from stars.models import Star, Type

class StarList(LoginRequiredMixin, generic.ListView) :
    def get(self, request):
        sc = Star.objects.all();
        tl = Type.objects.all().count();

        ctx = { 'type_count': tl, 'star_list': sc };
        return render(request, 'stars/star_list.html', ctx)

class StarCreate(LoginRequiredMixin,CreateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars')

class StarUpdate(LoginRequiredMixin, UpdateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars')

class StarDelete(LoginRequiredMixin, DeleteView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars')



class TypeList(LoginRequiredMixin, generic.ListView) :
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars')

class TypeCreate(LoginRequiredMixin,CreateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars')

class TypeUpdate(LoginRequiredMixin, UpdateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars')

class TypeDelete(LoginRequiredMixin, DeleteView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars')


