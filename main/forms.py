# forms.py
from django import forms
from .models import *


class GeneralInformationForm(forms.Form):
    university_type = forms.MultipleChoiceField(
        choices=[('', 'Hepsi')] + [(choice, choice) for choice in
                                   GeneralInformation.objects.values_list('üniversite_türü',
                                                                          flat=True).distinct()],
        required=False,
        label='Universite Türü'
    )
    university_name = forms.MultipleChoiceField(
        choices=[('', 'Hepsi')] + [(choice, choice) for choice in
                                   GeneralInformation.objects.values_list('üniversite',
                                                                          flat=True).distinct()],
        required=False,
        label='üniversite'
    )
    major_name = forms.MultipleChoiceField(
        choices=[('', 'Hepsi')] + [(choice, choice) for choice in
                                   GeneralInformation.objects.values_list('bolum_adi',
                                                                          flat=True).distinct()],
        required=False,
        label='Bölüm'
    )
    year = forms.MultipleChoiceField(
        choices=[('', 'Hepsi')] + [(choice, choice) for choice in
                                   GeneralInformation.objects.values_list('yil',
                                                                          flat=True).distinct()],
        required=False,
        label='Yıl'
    )
    scholarship = forms.MultipleChoiceField(
        choices=[('', 'Hepsi')] + [(choice, choice) for choice in
                                   GeneralInformation.objects.values_list('burs_türü',
                                                                          flat=True).distinct()],
        required=False,
        label='Burs Türü'
    )


class PreferenceTendencyFilterForm(forms.Form):
    university = forms.MultipleChoiceField(
        choices=[('', 'Hepsi')] + [(choice, choice) for choice in
                                   VwPreferenceTendencySamePrograms.objects.values_list('üniversite', flat=True).distinct()],
        required=False,
        label='Üniversite'
    )
    major_name = forms.MultipleChoiceField(
        choices=[('', 'Hepsi')] + [(choice, choice) for choice in
                                   VwPreferenceTendencySamePrograms.objects.values_list('bolum_adi', flat=True).distinct()],
        required=False,
        label='Bölüm Adı'
    )
    year = forms.MultipleChoiceField(
        choices=[('', 'Hepsi')] + [(choice, choice) for choice in
                                   VwPreferenceTendencySamePrograms.objects.values_list('yil', flat=True).distinct()],
        required=False,
        label='Yıl'
    )
