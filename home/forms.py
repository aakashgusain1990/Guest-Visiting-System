from django import forms
from .models import facultyt, securityt, visitort
class facultyForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,max_length=50)
    class Meta:
        model = facultyt
        fields = ["name","username","email","password"]
class securityForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,max_length=50)
    class Meta:
        model = securityt
        fields = ["name","username","email","password"]
class loginForm(forms.Form):
    username = forms.CharField(label = "Username",max_length=50)
    password = forms.CharField(label = "Password",widget=forms.PasswordInput,max_length=50) 
class visitorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,max_length=50)
    class Meta:
        model = visitort
        fields = ["name","dob","gender","username","email","password","govt_id"]
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