from django import forms
from .models import facultyt, securityt, visitort
class facultyForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,max_length=50)
    class Meta:
        model = facultyt
        fields = ["name","username","email","password"]
        def __init__(self, *args, **kwargs):
            super(facultyForm, self).__init__(*args, **kwargs)
            self.fields.widget.attrs.update({'class' : 'dee'})
class securityForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,max_length=50)
    class Meta:
        model = securityt
        fields = ["name","username","email","password"]
        def __init__(self, *args, **kwargs):
            super(securityForm, self).__init__(*args, **kwargs)
            self.fields.widget.attrs.update({'class' : 'dee'})
class loginForm(forms.Form):
    username = forms.CharField(label = "Username",max_length=50,widget=forms.TextInput(attrs={'class' : 'k'}))
    password = forms.CharField(label = "Password",max_length=50,widget=forms.PasswordInput(attrs={'class' : 'k'})) 
   
class visitorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,max_length=50)
    class Meta:
        model = visitort
        fields = ["name","dob","gender","username","email","password","govt_id"]
        def __init__(self, *args, **kwargs):
            super(visitorForm, self).__init__(*args, **kwargs)
            self.fields.widget.attrs.update({'class' : 'dee'})
class appointmentForm(forms.Form):
    doa = forms.DateField(label='Date of Appointment')
    timeIn = forms.TimeField(label='Time of Appointment')
    purpose = forms.CharField(widget=forms.Textarea,label='Purpose')
    

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if faculty.objects.get(email=email).exists():
#             raise ValidationError("Email already exists")
#         return email
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if faculty.objects.get(username=username).exists():
#             raise ValidationError("Email already exists")
#         return username

# class securityForm(forms.Form):
#     name = forms.CharField(label = "Name",max_length=50)
#     username = forms.CharField(label = "Username",max_length=50)
#     email = forms.CharField(label = "Email",max_length=50)
#     password = forms.CharField(label = "Password",widget=forms.PasswordInput,max_length=50)
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.get(email=email).exists():
#             raise ValidationError("Email already exists")
#         return email
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if User.objects.get(username=username).exists():
#             raise ValidationError("Email already exists")
#         return username