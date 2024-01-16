from django.views.generic.edit import FormView, CreateView
from .models import Review, Campaign, Vaccine, DoseBooking, AvailableTime
from .forms import CampaignReviewForm, VaccineForm, DoseBookingForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from datetime import timedelta
from django.urls import reverse
from django.contrib import messages


class VaccineCreateView(CreateView):
    model = Vaccine
    form_class = VaccineForm
    template_name = "vaccine_create.html"
    success_url = reverse_lazy("vaccine_list")

    def form_valid(self, form):
        form.instance.user_account = self.request.user.account
        messages.success(self.request, "Vaccine Created Successfully!! Thank You!!")
        return super().form_valid(form)


class VaccineListView(ListView):
    model = Vaccine
    template_name = "vaccine_list.html"
    context_object_name = "vaccine_list"
    ordering = ["-date"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class VaccineUpdateView(UpdateView):
    model = Vaccine
    form_class = VaccineForm
    template_name = "vaccine_update.html"
    success_url = reverse_lazy("vaccine_list")


class VaccineDeleteView(DeleteView):
    model = Vaccine
    template_name = "vaccine_confirm_delete.html"
    success_url = reverse_lazy("vaccine_list")


class DoseBookingCreateView(LoginRequiredMixin, CreateView):
    model = DoseBooking
    form_class = DoseBookingForm
    template_name = "dosebooking.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.patient = self.request.user
        form.instance.second_dose = form.instance.first_dose.date + timedelta(days=21)
        messages.success(self.request, "Dose Booking Successfully!! Thank You!!")
        return super().form_valid(form)


class CampaignReviewView(LoginRequiredMixin, FormView):
    template_name = "campaign_review.html"
    form_class = CampaignReviewForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        campaign = Campaign.objects.get(pk=self.kwargs["pk"])
        reviewer = self.request.user
        new_comment = form.save(commit=False)
        new_comment.campaign = campaign
        new_comment.reviwer = reviewer
        new_comment.save()
        messages.success(self.request, "Add Review Successfully!! Thank You!!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        campaign = Campaign.objects.get(pk=self.kwargs["pk"])
        reviews = campaign.reviews.all()
        comment_form = kwargs.get("form", CampaignReviewForm())
        context["reviews"] = reviews
        context["comment_form"] = comment_form
        return context
