from django_tables2 import Table, TemplateColumn
from rest_framework.renderers import TemplateHTMLRenderer

from funds.models import Fund


class FundTable(Table):
    inception_date = TemplateColumn('{{ record.inception_date|default_if_none:"—" }}')

    class Meta:
        model = Fund


class ListFundHTMLRenderer(TemplateHTMLRenderer):
    def get_template_context(self, *args, **kwargs):
        context = super().get_template_context(*args, **kwargs)
        total_aum = sum([fund["aum"] for fund in context if fund.get("aum")])
        formatted_total_aum = "{:.2f}".format(total_aum / 100)
        strategy_options = Fund.Strategies
        context = {
            "funds": FundTable(context),
            "fund_count": len(context),
            "strategy_options": strategy_options,
            "total_aum": formatted_total_aum,
        }
        return context
