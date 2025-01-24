from django import forms
from .models import Campaign, Donation

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['title', 'description', 'target_amount', 'end_date', 'image']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount']