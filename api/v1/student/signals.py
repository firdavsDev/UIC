# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.db.models import Sum 
# from .models import *

# #handling signals
# @receiver(post_save, sender=Student)
# def student_sponsor_handler(sender, instance, created, **kwargs):
#     student = Student.objects.get(pk=instance.pk)
#     if  student.sponsors_allocated_amount.all().count() > 0:
#         student.total_allocated_amount = student.sponsors_allocated_amount.aggregate(Sum('amount'))['amount__sum']
#         print(student.sponsors_allocated_amount.aggregate(Sum('amount'))['amount__sum'] )
#     instance.save()
