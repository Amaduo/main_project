from django.contrib import admin


from . models import Subscribe, Reservation, Message, Order


admin.site.register(Subscribe)

admin.site.register(Reservation)

admin.site.register(Message)

admin.site.register(Order)
# Register your models here.
