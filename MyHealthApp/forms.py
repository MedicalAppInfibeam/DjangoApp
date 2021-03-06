# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .models import *
from django import forms
from .choices import *
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class DocumentForm(forms.ModelForm):
    doc = forms.FileField(required=True, label='Upload Document', widget=forms.FileInput(attrs={'class':'choose-button'}))
    notes = forms.CharField(required=False, label='Notes', widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))

    class Meta:
        model = Document
        fields = ('doc', 'notes')


class InsuranceForm(forms.ModelForm):
    insurance_plan = forms.CharField(required=True, label='Insurance Plan', widget=forms.TextInput(attrs={'class':'my-label-desc'}))
    expiry_date = forms.DateField(required=True, label='Expiry Date', widget=forms.DateInput(attrs={'class':'my-label-desc'}))
    start_date = forms.DateField(required=True, label='Start Date', widget=forms.DateInput(attrs={'class':'my-label-desc'}))
    premium = forms.IntegerField(required=True, label='Premium Amount', widget=forms.NumberInput(attrs={'class':'my-label-desc'}))
    notes = forms.CharField(required=False, label='Notes', widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))

    class Meta:
        model = Insurance
        fields = ('insurance_plan', 'expiry_date', 'start_date', 'premium', 'notes')


class MeasurementForm(forms.ModelForm):
    blood_pressure = forms.CharField(required=False, label='Blood Pressure', widget=forms.TextInput(attrs={'class' : 'my-label-desc'}))
    blood_sugar = forms.CharField(required=False, label='Blood Sugar', widget=forms.TextInput(attrs={'class' : 'my-label-desc'}))
    cholesterol = forms.CharField(required=False, label='Cholesterol', widget=forms.TextInput(attrs={'class' : 'my-label-desc'}))
    height = forms.FloatField(required=True, label='Height', widget=forms.NumberInput(attrs={'class':'my-label-desc'}) )
    weight = forms.FloatField(required=True, label='Weight', widget=forms.NumberInput(attrs={'class':'my-label-desc'}))
    notes = forms.CharField(required=False, label='Notes', widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))

    class Meta:
        model = Measurement
        fields = ('blood_pressure', 'blood_sugar', 'cholesterol', 'height', 'weight', 'notes', 'date')


class DoctorForm(forms.ModelForm):
    doctor_name = forms.CharField(required=True, label='Name', widget=forms.TextInput(attrs={'class' : 'my-label-desc'}))
    doctor_description = forms.CharField(required=False, label='Description', widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))
    doctor_address = forms.CharField(required=True, label='Address', widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))
    doctor_speciality = forms.ChoiceField(required=True, choices=SPECIALITY_CHOICE, label='Speciality', widget=forms.Select(attrs={'class' : 'my-label-desc'}))
    doctor_timings = forms.CharField(required=True, label='Timing', widget=forms.TextInput(attrs={'class' : 'my-label-desc'}))
    doctor_pic = forms.ImageField(required=False, label='Upload Photo')
    doctor_phone_number = PhoneNumberField(required=False, label='Contact No.',widget=PhoneNumberPrefixWidget(attrs={'class':'my-label-phone'}))


    class Meta:
        model = Doctor
        fields = ( 'doctor_name', 'doctor_description', 'doctor_address', 'doctor_speciality', 'doctor_timings', 'doctor_pic', 'doctor_phone_number' )\
        
        
class DoctorNoteForm(forms.ModelForm):
    doctor_note = forms.CharField(required=False, label='Notes', widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))

    class Meta:
        model = Doctor_Note
        fields = ('doctor_note',)



class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.none(), label='Doctor', widget=forms.Select(attrs={'class' : 'my-label-desc'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class' : 'my-label-desc'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class' : 'my-label-desc'}))
    reason = forms.CharField(required=False, label='Reason', widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))
    notes = forms.CharField(required=False, label='Notes', widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))

    class Meta:
        model = Appointment
        fields = ('doctor', 'date', 'time', 'reason', 'notes')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].queryset = user.doctor_set.all()


class MedicineForm(forms.ModelForm):
    medicine_name = forms.CharField(required=True, label='Name', widget=forms.TextInput(attrs={'class' : 'my-label-desc'}))
    method = forms.ChoiceField(required=True, choices=MEDICINE_CHOICES, widget=forms.Select(attrs={'class' : 'my-label-desc'}))
    dosage_amt = forms.CharField(required=True, label='Amount', widget=forms.TextInput(attrs={'class' : 'my-label-desc', 'id':'my-label-desc-id'}))
    frequency = forms.IntegerField(help_text='No of times a day', required=True, label='Frequency', widget=forms.NumberInput(attrs={'class' : 'my-label-desc', 'id':'my-label-desc-id'}))
    medicine_date = forms.DateField(help_text='Start date of the prescription', required=False, label='Start Date', widget=forms.DateInput(attrs={'class':'my-label-desc'}))
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.none(), label='Doctor', widget=forms.Select(attrs={'class':'my-label-desc'}))
    usage_instructions = forms.CharField(required=True, label='Usage Instruction',  widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))
    overdose_instructions = forms.CharField(required=False, label='Overdose Instruction', widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))
    possible_sideeffects = forms.CharField(required=False, label='Possible Sideffects', widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))
    brand_names = forms.CharField(required=True, label='Brand Name', widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))


    class Meta:
        model = Medicine
        fields = (
            'medicine_name', 'method', 'dosage_amt', 'frequency', 'medicine_date', 'doctor', 'usage_instructions',
            'overdose_instructions', 'possible_sideeffects', 'brand_names')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MedicineForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].queryset = user.doctor_set.all()

class MedicineNoteForm(forms.ModelForm):
    medicine_note = forms.CharField(required=False, label='Notes', widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))

    class Meta:
        model = Medicine_Note
        fields = ('medicine_note',)


class DiseaseForm(forms.ModelForm):
    disease_name = forms.CharField(required=True, label='Name',widget=forms.TextInput(attrs={'class':'my-label-desc'}))
    disease_date = forms.DateField(required=True, label='Date', widget=forms.DateInput(attrs={'class':'my-label-desc'}))
    symptom = forms.ModelMultipleChoiceField(required=True, label='Symptom', queryset=Symptom.objects.all(), widget=forms.SelectMultiple(attrs={'class':'my-label-desc'}))
    medicine = forms.ModelMultipleChoiceField(required=True, label='Medicine', queryset=Medicine.objects.none(), widget=forms.SelectMultiple(attrs={'class':'my-label-desc'}))
    procedure = forms.ModelMultipleChoiceField(required=True, label='Procedure', queryset=Procedure.objects.all(), widget=forms.SelectMultiple(attrs={'class':'my-label-desc'}))
    disease_description = forms.CharField(required=False, label='Description', widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DiseaseForm, self).__init__(*args, **kwargs)
        self.fields['medicine'].queryset = user.medicine_set.all()

    class Meta:
        model = Disease
        exclude = ['user']

class DiseaseNoteForm(forms.ModelForm):
    disease_note = forms.CharField(required=False, label='Notes', widget=forms.Textarea(attrs={'class':'my-label-desc label-desc-text-area'}))

    class Meta:
        model = Disease_Note
        fields = ('disease_note',)
