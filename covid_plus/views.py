from django.shortcuts import render
from campaign.models import Campaign
from campaign.models import Review, Campaign
from campaign.forms import CampaignReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

# Create your views here.


# class CampaignListView(ListView):
#     model = Campaign
#     template_name = "home.html"
#     context_object_name = "campaigns"


# class CampaignReviewView(LoginRequiredMixin, FormView):
#     template_name = "home.html"
#     form_class = CampaignReviewForm
#     success_url = reverse_lazy("home")

#     def form_valid(self, form):
#         reviewer = self.request.user
#         new_comment = form.save(commit=False)
#         new_comment.reviwer = reviewer
#         new_comment.save()
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()  # Fetch all reviews
#         comment_form = kwargs.get("form", CampaignReviewForm())
#         context["reviews"] = reviews
#         context["comment_form"] = comment_form
#         return context


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
