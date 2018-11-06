from django import forms
from  django.core import validators

# CUSTOM VALIDATOR
# def check_name_i(value):
#     if value [0].lower() != 'i':
#         raise forms.ValidationError('Name start with the Letter I')


class formName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=True)
    verify_mail = forms.EmailField(label="Verify email again")
    text = forms.CharField(widget=forms.Textarea, required=True)
   # botcatcher = forms.CharField(required=True, widget=forms.Textarea, validators=[validators.MaxLengthValidator(0)])



    def clean(self):
        clean_all = super().clean()
        email = clean_all['email']
        vmail = clean_all['verify_mail']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAIL MATCH")
