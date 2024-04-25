from django import forms
from django.forms import ModelForm, DateInput
from tempus_dominus.widgets import DateTimePicker
from calender.models import Case
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm



TRUE_FALSE_CHOICES = (
    ('default', '-------'),
    (True, 'Yes'),
    (False, 'No')
)

class CaseForm(forms.ModelForm):

    i_589_filed = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, 
                    label="I 589 Filed ?", widget=forms.Select(attrs={
                                         'class': "form-select text-center fw-bold",
                                         
                                     }), required=True)
    erop = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, 
                    label="erop ?", widget=forms.Select(attrs={
                                         'class': "form-select text-center fw-bold",
                                         
                                     }), required=True)
    e_28_filed = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, 
                    label="e28 Filed ?", widget=forms.Select(attrs={
                                         'class': "form-select text-center fw-bold",
                                         
                                     }), required=True)
    biometrics_filed = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, 
                    label="Biometrics Filed ?", widget=forms.Select(attrs={
                                         'class': "form-select text-center fw-bold",
                                     }), required=True)
    foia_submitted = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, 
                    label="Foia Submitted ?", widget=forms.Select(attrs={
                                         'class': "form-select text-center fw-bold",
                                         
                                     }), required=True)
    foia_uploaded = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, 
                    label="Foia uploaded ?", widget=forms.Select(attrs={
                                         'class': "form-select text-center fw-bold",
                                         
                                     }), required=True)
    work_permit_applied = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, 
                    label="work permit applied ?", widget=forms.Select(attrs={
                                         'class': "form-select text-center fw-bold",
                                     }), required=True)    
    
    class Meta:
        model = Case
        fields = ["alien_number", "first_name", "middle_name", "last_name", "phone_number", "email", "Address", 
                  "city","zipcode","country","type_of_case", "i_589_filed", "erop", "e_28_filed", "biometrics_filed", "foia_submitted", 
                  "foia_uploaded", "work_permit_applied", "hearing_location", "total_billing_amount", 
                  "amount_paid", "date"]

        widgets = {
            "alien_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Alien Number"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your first name"}
            ),
            "middle_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your middle name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your last name"}
            ),

            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your phone number"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter your email"}
            ),
            "Address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your Address"}
            ),
            "city": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your city"}
            ),
            "zipcode": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your zipcode"}
            ),
            "country": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your country"}
            ),
            "type_of_case": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your last name"}
            ),

            "hearing_location": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your hearing location"}
            ),
            "total_billing_amount": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your total billing amount"}
            ),
            "amount_paid": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Amount Paid", 'value': '0'}#, "disabled":True}
            ),
            "date": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%d %H:%M",
            ),
            # "documents":forms.ClearableFileInput(attrs={"class": "form-control-file"})
        }
        exclude = ["user"]


    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        self.fields["date"].input_formats = ("%Y-%m-%d %H:%M",)


