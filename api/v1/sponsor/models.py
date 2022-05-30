from django.db import models

## Sponsor model
class Sponsor(models.Model):
    type_of_sponsor = (
        ('jismoniy shaxs', 'Jismoniy shaxs'),
        ('yuridik shaxs', 'Yuridik shaxs'),
    )
    sponsor_type = models.CharField(max_length=60, choices=type_of_sponsor)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100, blank=True, null=True, help_text='Tashkilot nomi')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status_choices = (
        ('1', 'Pending'),
        ('2', 'Accepted'),
        ('3', 'Rejected'),
    )
    status = models.CharField(choices=status_choices, default=1, max_length=1)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'sponsor'
        ordering = ['-created_at']
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'
        
        
## Sponsor allocate amount model
class SponsorAllocateAmount(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='sponsor_allocate_amount')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.sponsor.full_name
    
    class Meta:
        db_table = 'sponsor_allocate_amount'
        ordering = ['-created_at']
        verbose_name = 'Sponsor allocate amount'
        verbose_name_plural = 'Sponsor allocate amounts'