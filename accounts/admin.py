from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, PerfilUsuario
from django.utils.html import format_html


class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','username','last_login','date_joined','is_active')
    list_display_links=('email','first_name','last_name')
    readonly_fields=('last_login','date_joined')
    ordering=('-date_joined',)
    filter_horizontal = ()
    list_filter=()
    fieldsets = ()

class PerfilUsuarioAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.foto_perfil.url))
    thumbnail.short_description = 'Foto de Perfil'
    list_display = ('thumbnail', 'user', 'ciudad', 'estado', 'pais')

admin.site.register(Account, AccountAdmin)
admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)