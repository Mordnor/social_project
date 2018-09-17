# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileInlineFormSet

from django.contrib.auth import authenticate, login


class IndexView(ListView):
    model = Profile

    def get_queryset(self):
        words_query = self.request.GET.get('q', None)
        if words_query is not None:
            return Profile.objects.filter(slug=words_query)
        else:
            return Profile.objects.all()


class ProfileDetailView(DetailView):
    model = Profile


class ProfileUpdateView(UpdateView):
    model = User
    slug_url_kwarg = 'username'
    slug_field = 'username'
    fields = ('username', 'first_name', 'last_name', 'email')
    template_name = 'codintalk/profile_update_form.html'

    def get_context_data(self, **kwargs):
        context = UpdateView.get_context_data(self, **kwargs)
        context["profile_formset"] = ProfileInlineFormSet(instance = self.get_object())
        return context

    def form_valid(self, form):
        formset =  ProfileInlineFormSet(self.request.POST, instance=self.get_object())
        if formset.is_valid():
            form.save()
            formset.save()

            return redirect(self.get_success_url())
        else: 
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('profile-detail', args=[self.get_object().profile.slug])


class ProfileAddFriend(View):

    def post(self, request, *args, **kwargs):
        current_user = request.user
        new_friend_id = request.POST.get('friend_id', None)

        current_profile = current_user.profile
        new_friend_profile = Profile.objects.get(id=new_friend_id)

        current_profile.friends.add(new_friend_profile)

        return redirect(reverse('profile-detail', args=[new_friend_profile.user.username]))