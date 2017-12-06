from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class AuthUserAdmin(UserAdmin):
    exclude = ('first_name', 'last_name')
    # Make 'email' and 'name' un-editable by admin
    readonly_fields = [
        'name',
        'email',
        'last_login',
        'date_joined',
    ]
    fieldsets = (
        ('Personal info', {'fields': ('name', 'username', 'email', 'password')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
                                    'is_superuser', 'groups', 'user_permissions')}),
    )


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
        # Intensely left blank.
        # To be used for displaying fields other than those
        # defined in AuthUserAdmin.
        # Uncomment the line below to see it yourself.

        # ('User Profile', {'fields': ('name',)}),
    ) + AuthUserAdmin.fieldsets
    # Display these items in all 'Users' list (Home>Users>Users)
    list_display = ('username', 'name', 'email', 'is_superuser')
    # Use these fields when I search the for a user
    search_fields = ['name', 'username', 'email']
