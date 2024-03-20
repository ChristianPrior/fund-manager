from io import TextIOWrapper

from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer

from funds.csv_uploader import csv_to_db
from funds.forms import UploadForm


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
