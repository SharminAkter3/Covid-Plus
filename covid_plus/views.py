from django.shortcuts import render
from campaign.models import Campaign
from campaign.models import Review, Campaign
from campaign.forms import CampaignReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

# Create your views here.


class HomeView(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        campaigns = Campaign.objects.all()
        reviews = Review.objects.all()
        comment_form = CampaignReviewForm()

        context = {
            "campaigns": campaigns,
            "reviews": reviews,
            "comment_form": comment_form,
        }

        return render(request, self.template_name, context)


def about(request):
    return render(request, "aboutUs.html")


def contact(request):
    return render(request, "contact.html")
