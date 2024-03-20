from io import TextIOWrapper

from django.shortcuts import render
from django_filters import rest_framework as filters
from django_tables2.views import SingleTableMixin
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from funds.csv_uploader import csv_to_db
from funds.forms import UploadForm
from funds.models import Fund
from funds.renderers import ListFundHTMLRenderer
from funds.serializers import FundSerializer


class FundListView(generics.ListAPIView, SingleTableMixin):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ("strategy",)
    renderer_classes = [JSONRenderer, ListFundHTMLRenderer]
    template_name = "list.html"


class FundView(generics.RetrieveAPIView):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer


class UploadView(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return render(request, "upload.html", {"form": UploadForm()})

    def post(self, request, *args, **kwargs):
        funds_file = request.FILES["funds_file"]
        fund_data = TextIOWrapper(funds_file, encoding="utf-8-sig", newline="")
        uploaded_fund_count, form_errors = csv_to_db(fund_data)

        return render(
            request,
            "upload.html",
            {
                "form": UploadForm(),
                "form_errors": form_errors,
                "uploaded_fund_count": uploaded_fund_count,
            },
        )
