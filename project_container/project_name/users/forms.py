from django import forms


class SignupForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Your full name'}))

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.save()
