from django.contrib import admin
from .models import Attendance, Meeting, Member, Contribution


class TrackerAdminMixin:
    """Makes admin read/write from the 'tracker' database instead of 'default'."""
    using = 'tracker'

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)


class MemberAdmin(TrackerAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'role', 'regno', 'emailid', 'joined_on')
    list_editable = ('role',)

class MeetingAdmin(TrackerAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'code', 'date', 'start_time', 'end_time')


class AttendanceAdmin(TrackerAdminMixin, admin.ModelAdmin):
    list_display = ('member_name', 'meeting_code', 'first_seen', 'duration')


class ContributionAdmin(TrackerAdminMixin, admin.ModelAdmin):
    pass


admin.site.register(Member, MemberAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Contribution, ContributionAdmin)