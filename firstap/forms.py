from django import forms
from .models import Country, Province

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"
        #fields = ("country_name", "country_code", "continent")

class ProvinceForm(forms.ModelForm):
    class Meta:
        model = Province
        fields = ("province_name",)