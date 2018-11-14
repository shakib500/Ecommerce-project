from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Your full name",
                        "style":"margin:10px 0; padding:10px"
                    }
                    )
            )
    email    = forms.EmailField(
            widget=forms.EmailInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Your email",
                        "style":"margin:10px 0; padding:10px"
                    }
                    )
            )
    content  = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    'class': 'form-control',
                    "placeholder": "Your message" ,
                    "style":"margin:10px 0; padding:10px"
                    }
                )
            )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email



# login form
class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class" : "form-control", "placeholder" : "Username", "style":"margin:10px 0; padding:10px"
            }
        )   
        )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class" : "form-control", "placeholder" : "password", "style":"margin:10px 0; padding:10px"
            }
        )
    )

#register form
class RegisterForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class" : "form-control", "placeholder" : "User Name", "style":"  margin:10px 0; padding:10px"
            }
        )
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                "class" : "form-control", "placeholder" : "Email", "style":" margin:10px 0; padding:10px"
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class" : "form-control", "style":" margin:10px 0; padding:10px"
            }
        )
    )
    password2 = forms.CharField(
        label = "Confirm password",
        widget = forms.PasswordInput(
            attrs={
                "class" : "form-control", "style":" margin:10px 0; padding:10px"
            }
        )
    )
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Passwords does not match.")
        return data














