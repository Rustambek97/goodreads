from django import forms
from users.models import CustomUser

class UserRegistrForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def save(self):
        super().save()
        user = CustomUser.objects.get(username=self.cleaned_data['username'])
        user.set_password(self.cleaned_data['password'])
        user.save()


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'profile_picture')
