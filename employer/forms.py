from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from employer.models import UserProfile

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(help_text='This E-mail Field is required')
    Keywords = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    experince = forms.IntegerField()
    phone = forms.IntegerField()
    price = forms.IntegerField()
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'Keywords',
            'description',
            'experince',
            'phone',
            'price',
            'password1',
            'password2',
            )

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=True)
            user.username = self.cleaned_data['username']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.Keywords = self.cleaned_data['Keywords']
            user.description = self.cleaned_data['description']
            user.experince = self.cleaned_data['experince']
            user.phone = self.cleaned_data['phone']
            user.price = self.cleaned_data['price']

            if commit:
                user.save()
            return user

'''
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']


        if commit:
            user.save()

        return user

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=('Keywords','description','experince','phone', 'price')

        def save(self, commit=True):
            employee = super(UserProfileForm, self).save(commit=False)
            #employee.username = self.cleaned_data['username']
            employee.Keywords = self.cleaned_data['Keywords']
            employee.description = self.cleaned_data['description']
            employee.experince = self.cleaned_data['experince']
            employee.phone = self.cleaned_data['phone']
            employee.price = self.cleaned_data['price']


            if commit:
                employee.save()

            return employee

'''

class EditProfileForm(UserChangeForm):
    template_name='accounts/edit_profile.html'

    class Meta:
        model = UserProfile
        fields = '__all__'
