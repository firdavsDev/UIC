from django.db import models
from api.v1.sponsor import models as sponsor_models

# Student model
class Student(models.Model):
    type_of_student = (
        ('bakalavr', 'Bakalavr'),
        ('magistr', 'Magistr'),
    )
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    otm = models.ForeignKey('Otm', on_delete=models.CASCADE, related_name='students_otm')
    sponsors = models.ManyToManyField(sponsor_models.Sponsor, related_name='students_sponsors', help_text='Homiylar', blank=True)
    student_type = models.CharField(max_length=60, choices=type_of_student)
    allocated_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        
    def __str__(self):
        return self.full_name

# OTM model
class OTM(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'otm'
        verbose_name = 'OTM'
        verbose_name_plural = 'OTMs'
    
    def __str__(self):
        return self.name
    