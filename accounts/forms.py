from django import forms
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter Your Password'
    }), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm Your Password'
    }), label='Confirm Password')

    class Meta:
        model = User
        fields = ['name', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1:
            raise ValidationError('پسورد اول خالی است!')
        if not password2:
            raise ValidationError("پسورد دوم خالی است!")
        if password1 != password2:
            raise ValidationError("پسودها یکی نیست!")

        return password2


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='برای عوض کردن پسورد  <a href=\"../password/\">کلیک کنید</a>.',
                                         label='رمز عبور')

    class Meta:
        model = User
        fields = ['name', 'email', 'is_admin', 'is_active']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter Your Email'
            })
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email)
        if user:
            raise ValidationError("this email already exists")
        return email


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=120,
                             widget=forms.EmailInput(attrs={'placeholder': "Enter a valid email address",
                                                            'class': 'form-control', }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter Your Password'}))
