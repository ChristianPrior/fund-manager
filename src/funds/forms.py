from django.forms import FileField, Form, ModelForm

from funds.models import Fund


class FundForm(ModelForm):
    class Meta:
        model = Fund
        fields = ["name", "strategy", "aum", "inception_date"]


class UploadForm(Form):
    funds_file = FileField()
