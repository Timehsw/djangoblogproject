# -*- coding: utf-8 -*-

from django import forms
from .models import Comment
'''
    Created by hushiwei on 2017/9/24.
'''

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','url','text']