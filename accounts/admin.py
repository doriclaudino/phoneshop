from django.contrib import admin
from accounts.models import User
from django.contrib.auth import models, forms
from django.contrib import auth

# admin.site.register(models.Group)


class UserCreateForm(forms.UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', )


class UserAdmin(auth.admin.UserAdmin):
    add_form = UserCreateForm
    prepopulated_fields = {'username': ('first_name', 'last_name', )}

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', ),
        }),
    )


# Re-register UserAdmin
admin.site.register(User, UserAdmin)
