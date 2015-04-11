__author__ = 'Dmitry'
# -*- coding: utf-8 -*-
from django import forms

class FileForm(forms.Form):
    content = forms.FileField(
        label='Select a file'
    )