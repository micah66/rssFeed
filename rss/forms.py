from django import forms

class SearchForm(forms.Form):
    search_criteria = forms.CharField(max_length=50)
