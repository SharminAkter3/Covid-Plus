from django.urls import path
from .views import (
    CampaignReviewView,
    VaccineCreateView,
    VaccineListView,
    VaccineUpdateView,
    VaccineDeleteView,
    DoseBookingCreateView,
)

urlpatterns = [
    # path("", CampaignListView.as_view(), name="campaign_list"),
    path("review/<int:pk>", CampaignReviewView.as_view(), name="campaign_review"),
    path("vaccine", VaccineCreateView.as_view(), name="vaccine"),
    path("vaccine_list/", VaccineListView.as_view(), name="vaccine_list"),
    path("vaccine/<int:pk>/edit/", VaccineUpdateView.as_view(), name="edit_vaccine"),
    path(
        "vaccine/<int:pk>/delete/", VaccineDeleteView.as_view(), name="delete_vaccine"
    ),
    path("booking/", DoseBookingCreateView.as_view(), name="booking"),
]
