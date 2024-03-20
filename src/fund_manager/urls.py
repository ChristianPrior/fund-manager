from django.contrib import admin
from django.urls import path

from funds.views import FundListView, FundView, UploadView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("funds/", FundListView.as_view()),
    path("funds/<int:pk>/", FundView.as_view()),
    path("funds/upload/", UploadView.as_view()),
]
