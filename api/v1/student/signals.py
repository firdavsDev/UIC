from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum, F
from .models import *

#handling signals
@receiver(post_save, sender=Student)
def add_student_sponsor_handler(sender, instance, **kwargs):
    post_save.disconnect(add_student_sponsor_handler, sender=sender)
    instance.total_allocated_amount = instance.sponsors_allocated_amount.all().aggregate(Sum('amount'))['amount__sum']
    instance.save()
    post_save.connect(add_student_sponsor_handler, sender=sender)

