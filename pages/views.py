from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django import forms
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView, ModelFormMixin
from django.urls import reverse, reverse_lazy
from .models import *
# from .forms import *
# from .services import *
from datetime import datetime
from django.contrib import messages
from django.conf import settings


def HomePageView(request):
	messages.success(request, 'Toastr marche !')

	return render(request, 'pages/home.html', {'test': 'ca marche'})


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'