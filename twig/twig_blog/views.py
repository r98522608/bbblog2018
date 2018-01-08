# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.


class HomeView2(TemplateView):
    myqq = True
    # def get_context_data(self,*args,**kwargs):
        # context = super(HomeView, self).get_context_data(*args,**kwargs)
        # return context

class HomeView(TemplateView):
    def get_context_data(self,*args,**kwargs):
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        return context



class ContactView(TemplateView):
    def get_context_data(self,*args,**kwargs):
        context = {
            'contact'    : 'contact',
            'mailhost'  :'max@hotmail.com',
        }
        return context

class AboutView(TemplateView):
    def get_context_data(self,*args,**kwargs):
        context = {
            'intro':    "We are TWIG",
        }
        return context


