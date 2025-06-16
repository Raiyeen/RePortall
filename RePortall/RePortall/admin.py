from django.contrib import admin

from .models import Customer, Review, ReportSubmission

admin.site.register(Customer)
admin.site.register(Review)
admin.site.register(ReportSubmission)
# admin.site.register(Tag)
