from django.db import models
from django.contrib.auth.models import User

class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    image = models.ImageField(upload_to='campaign_images/')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Donation(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor.username} - {self.amount}"

class Report(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    report_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"Report for {self.campaign.title} on {self.report_date}"