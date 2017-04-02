from django.contrib import admin
from contactform.models import Contact

class ContactAdmin(admin.ModelAdmin):
	#list_filter = ('nick', 'user')
	list_display = ('name', 'email', 'data')

admin.site.register(Contact, ContactAdmin)
