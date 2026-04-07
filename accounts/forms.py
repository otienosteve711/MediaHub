from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from .models import User
# registration form
class UserRegistrationForm(UserCreationForm):
    # customizing our inputs for the registration form
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    user_type = forms.ChoiceField(choices=User.USER_TYPE_ROLES, widget=forms.Select(attrs={'class': 'form-control'}))
    # create a subclass called meta
    # Here we mention the fields to be filled in our form
    class Meta:
        model = User
        fields = ('username', 'email', 'user_type', 'password1', 'password2')#simply indicates the fields to be filled in our form: fields should be attributes in the models.py
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Username'
            }),
        }# here customizing our input fields if not overriden before meta class
        # passwords matching check
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['password1'].widget.attrs.update(
                {
                    'class':'form-control',
                    'placeholder':'Password'
                }
            )
            self.fields['password2'].widget.attrs.update(
                {
                    'class':'form-control',
                    'placeholder':'Confirm Password'
                }
            )
#override for the user authentication form
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }
    ))
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'bio', 'profile_image')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 3
            }),
        }         

    