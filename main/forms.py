# forms.py
from django import forms
from .models import *


class YourModelFilterForm(forms.Form):
    university_type = forms.ChoiceField(
        choices=[('', 'All University Types')] + [(choice, choice) for choice in
                                                  GenelBilgilerLast2024.objects.values_list('üniversite_türü',
                                                                                            flat=True).distinct()],
        required=False,
        label='University Type'
    )
    university_name = forms.ChoiceField(
        choices=[('', 'All Universities')] + [(choice, choice) for choice in
                                              GenelBilgilerLast2024.objects.values_list('üniversite',
                                                                                        flat=True).distinct()],
        required=False,
        label='University'
    )
    year = forms.ChoiceField(
        choices=[('', 'All Years')] + [(choice, choice) for choice in
                                              GenelBilgilerLast2024.objects.values_list('yil',
                                                                                        flat=True).distinct()],
        required=False,
        label='Yıl'
    )


class CompareUniversitiesForm(forms.Form):
    university_name_left = forms.ChoiceField(
        choices=[('', 'All Universities')] + [(choice, choice) for choice in
                                              GenelBilgilerLast2024.objects.values_list('üniversite', flat=True).distinct()],
        required=False,
        label='Left University'
    )
    university_name_right = forms.ChoiceField(
        choices=[('', 'All Universities')] + [(choice, choice) for choice in
                                              GenelBilgilerLast2024.objects.values_list('üniversite', flat=True).distinct()],
        required=False,
        label='Right University'
    )
    major_name_left = forms.ChoiceField(
        choices=[('', 'Tüm Bölümler')] + [(choice, choice) for choice in
                                              GenelBilgilerLast2024.objects.values_list('bolum_adi', flat=True).distinct()],
        required=False,
        label='Left University'
    )
    major_name_right = forms.ChoiceField(
        choices=[('', 'Tüm Bölümler')] + [(choice, choice) for choice in
                                              GenelBilgilerLast2024.objects.values_list('bolum_adi', flat=True).distinct()],
        required=False,
        label='Right University'
    )
    university_type_left = forms.ChoiceField(
        choices=[('', 'All University Types')] + [(choice, choice) for choice in
                                                  GenelBilgilerLast2024.objects.values_list('üniversite_türü', flat=True).distinct()],
        required=False,
        label='Left University Type'
    )
    university_type_right = forms.ChoiceField(
        choices=[('', 'All University Types')] + [(choice, choice) for choice in
                                                  GenelBilgilerLast2024.objects.values_list('üniversite_türü', flat=True).distinct()],
        required=False,
        label='Right University Type'
    )
    year_left = forms.ChoiceField(
        choices=[('', 'All Years')] + [(choice, choice) for choice in
                                       GenelBilgilerLast2024.objects.values_list('yil', flat=True).distinct()],
        required=False,
        label='Left Year'
    )
    year_right = forms.ChoiceField(
        choices=[('', 'All Years')] + [(choice, choice) for choice in
                                       GenelBilgilerLast2024.objects.values_list('yil', flat=True).distinct()],
        required=False,
        label='Right Year'
    )