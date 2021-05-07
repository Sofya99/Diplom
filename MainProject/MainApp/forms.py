from django import forms
from .models import sut_sum_diff_srNew

class FindName(forms.Form):
    NameStation = forms.CharField(max_length=50)
