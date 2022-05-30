from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum, F
from .models import *

#handling signals (not finished yet)
@receiver(post_save, sender=SponsorAllocateAmount)
def calculate_sponsor_sum(sender, instance, **kwargs):
    post_save.disconnect(calculate_sponsor_sum, sender=sender)
    extra_sum = instance.sponsor.amount - instance.amount
    print(instance.sponsor.amount)
    print(instance.amount)
    print(extra_sum)
    instance.save()
    instance.sponsor.save()
    post_save.connect(calculate_sponsor_sum, sender=sender)

