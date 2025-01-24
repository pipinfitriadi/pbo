from django.shortcuts import render, redirect
from .models import Campaign, Donation
from .forms import CampaignForm, DonationForm
from django.contrib.auth.decorators import login_required

def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'campaigns/campaign_list.html', {'campaigns': campaigns})

@login_required
def create_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.creator = request.user
            campaign.save()
            return redirect('campaign_list')
    else:
        form = CampaignForm()
    return render(request, 'campaigns/create_campaign.html', {'form': form})

@login_required
def donate(request, campaign_id):
    campaign = Campaign.objects.get(id=campaign_id)
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.campaign = campaign
            donation.donor = request.user
            donation.save()
            campaign.current_amount += donation.amount
            campaign.save()
            return redirect('campaign_list')
    else:
        form = DonationForm()
    return render(request, 'campaigns/donate.html', {'form': form, 'campaign': campaign})
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('campaign_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})