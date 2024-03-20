from csv import DictReader

from django.db import transaction

from funds.forms import FundForm


def csv_to_db(file_contents):
    form_errors = []
    funds_to_create = []
    for index, row in enumerate(DictReader(file_contents), 2):
        cleaned_fund_data = {
            "name": row["Name"],
            "strategy": row["Strategy"],
            "aum": row["AUM (USD)"],
            "inception_date": row["Inception Date"],
        }

        form = FundForm(cleaned_fund_data)
        if form.is_valid():
            funds_to_create.append(form)
        else:
            form_errors.append(f"Row: {index}, Errors: {form.errors.as_json()}")
            continue

    if form_errors:
        return 0, form_errors

    with transaction.atomic():
        for fund in funds_to_create:
            fund.save()

    return len(funds_to_create), None
