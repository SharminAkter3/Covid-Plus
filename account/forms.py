from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserAccount, GENDER_TYPES, ROLE_CHOICES
from django.contrib.auth.forms import PasswordChangeForm


class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    nid = forms.CharField(max_length=20)
    gender = forms.ChoiceField(choices=GENDER_TYPES)
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "nid",
            "gender",
            "role",
            "postal_code",
            "city",
            "street_address",
            "country",
        ]

    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            nid = self.cleaned_data.get("nid")
            gender = self.cleaned_data.get("gender")
            role = self.cleaned_data.get("role")
            postal_code = self.cleaned_data.get("postal_code")
            country = self.cleaned_data.get("country")
            birth_date = self.cleaned_data.get("birth_date")
            city = self.cleaned_data.get("city")
            street_address = self.cleaned_data.get("street_address")

            UserAccount.objects.create(
                user=our_user,
                nid=nid,
                gender=gender,
                role=role,
                birth_date=birth_date,
                postal_code=postal_code,
                country=country,
                city=city,
                street_address=street_address,
            )
        return our_user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": (
                        "appearance-none block w-full bg-white "
                        "text-black border border-gray-200 rounded "
                        "py-3 px-4 leading-tight focus:outline-none "
                        "focus:bg-white focus:border-gray-500"
                    )
                }
            )


class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    gender = forms.ChoiceField(choices=GENDER_TYPES, required=False)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": (
                        "appearance-none block w-full bg-white "
                        "text-black border border-gray-200 rounded "
                        "py-3 px-4 leading-tight focus:outline-none "
                        "focus:bg-white focus:border-gray-500"
                    )
                }
            )
        if self.instance:
            try:
                user_account = self.instance.account
            except UserAccount.DoesNotExist:
                user_account = None

            if user_account:
                self.fields["gender"].initial = user_account.gender
                self.fields["birth_date"].initial = user_account.birth_date
                self.fields["street_address"].initial = user_account.street_address
                self.fields["city"].initial = user_account.city
                self.fields["postal_code"].initial = user_account.postal_code
                self.fields["country"].initial = user_account.country

                self.fields["role"].initial = user_account.role

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_account, created = UserAccount.objects.get_or_create(user=user)
            user_account.gender = self.cleaned_data["gender"]
            user_account.birth_date = self.cleaned_data["birth_date"]
            user_account.street_address = self.cleaned_data["street_address"]
            user_account.city = self.cleaned_data["city"]
            user_account.postal_code = self.cleaned_data["postal_code"]
            user_account.country = self.cleaned_data["country"]

            user_account.role = self.cleaned_data["role"]
            user_account.save()

        return user


class StyledPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": (
                        "appearance-none block w-full bg-white "
                        "text-black border border-gray-200 rounded "
                        "py-3 px-4 leading-tight focus:outline-none "
                        "focus:bg-white focus:border-gray-500"
                    )
                }
            )
