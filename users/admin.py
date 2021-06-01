from django.contrib import admin
from .models import Costumer
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, NumberInput
# Register your models here.


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'username', 'firstname', 'lastname')
    list_filter = ('email', 'username', 'firstname', 'lastname', 'is_active', 'is_staff')
    ordering= ('start_date',)
    list_display = ('email', 'username','firstname', 'lastname', 'investing_style')
    fieldsets = (
        (None, {'fields':('email', 'username', 'firstname', 'lastname','investing_style', 'password') }),
        ('Permission', {'fields':('is_active','is_staff',) }),
        ('Personal', {'fields':('contact','about',) }),
    )
    formfield_overrides={
        Costumer.contact:{'widget': NumberInput(attrs={'style':'width:40px'})},
        Costumer.about: {'widget': Textarea(attrs={'rows':10,'cols':40})}
    }
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields': ('email', 'username', 'password1','password2','firstname', 'lastname','contact', 'investing_style', 'is_active', 'is_staff')
            }
        ),
    )
admin.site.register(Costumer, UserAdminConfig)