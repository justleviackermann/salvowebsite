from django.contrib import admin
from website.models import Post, Account, Member


class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('password',)  # Don't allow raw hash editing


class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ('password',)  # Don't allow raw hash editing
    list_display = ('name', 'register_no', 'club_role', 'batch', 'branch')
    list_editable = ('club_role',)  # Change role directly from the list view


admin.site.register(Post)
admin.site.register(Account, AccountAdmin)
admin.site.register(Member, MemberAdmin)