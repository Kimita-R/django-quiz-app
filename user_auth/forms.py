from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


# Create your forms here.
class NewUserForm(UserCreationForm):

	username = forms.CharField(
		widget = TextInput(attrs={
			'class': 'form-control',
            'required': 'true',
            'placeholder': 'Username'
    	})
	)

	email = forms.EmailField(
		widget = EmailInput(attrs={
			'class': 'form-control',
			'type': 'email',
            'required': 'true',
            'placeholder': 'Email'
   		})
	)

	password1 = forms.CharField(
		widget = TextInput(attrs={
			'class': 'form-control',
			'type': 'password',
            'required': 'true',
            'placeholder': 'Password'
   		})
	)

	password2 = forms.CharField(
		widget = TextInput(attrs={
			'class': 'form-control',
			'type': 'password',
            'required': 'true',
            'placeholder': 'Re-enter Password'
   		})
	)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.username = self.cleaned_data["username"]
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user