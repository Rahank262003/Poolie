from django.contrib import admin
from Poolie.models import Registration
from Poolie.models import Publishride
from Poolie.models import Contact
from Poolie.models import Passenger

# Register your models here.
admin.site.register(Registration)
admin.site.register(Publishride)
admin.site.register(Contact)
admin.site.register(Passenger)

