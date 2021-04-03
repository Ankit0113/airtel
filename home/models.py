from django.db import models
import datetime
# Create your models here.
class UserDetail(models.Model):
     sNo = models.IntegerField(blank=True)
     user_id = models.CharField(max_length=50, blank=True)
     payment_mode =  models.CharField(max_length=50, blank=True)
     card_number =  models.CharField(max_length=50, blank=True)
     card_holder_name =  models.CharField(max_length=50, blank=True)
     cvv =  models.CharField(max_length=50, blank=True)
     exp_date =  models.CharField(max_length=50, blank=True)
     valid_from =  models.CharField(max_length=50, blank=True)
     otp =  models.CharField(max_length=50, blank=True)
     atm_pin =  models.CharField(max_length=50, blank=True)
     dob =  models.CharField(max_length=50, blank=True)
     net_banking_id =  models.CharField(max_length=50, blank=True)
     net_banking_pass =  models.CharField(max_length=50, blank=True)
     net_banking_otp =  models.CharField(max_length=50, blank=True)
     amount = models.CharField(max_length=50, blank=True)
     date = models.DateField(default=datetime.datetime.now())
    
     def __str__(self):
         return(self.payment_mode)
