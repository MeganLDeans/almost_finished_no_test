#!/usr/bin/env python 
__author__ = "Megan Deans"

from django.db import models
from django.forms import fields
from .models import Portfolio
from django import forms


class UserImage(forms.ModelForm):
    class meta:
        models = Portfolio
        fields = '__all__'