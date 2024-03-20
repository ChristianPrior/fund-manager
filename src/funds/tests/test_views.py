from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from funds.models import Fund

TEST_FUND_DATA = {
    "name": "test",
    "strategy": "Arbitrage",
    "aum": 1000,
    "currency_code": "USD",
    "inception_date": "2024-03-19",
}


class ListFundsTest(TestCase):
    def test_list_funds(self):
        test_fund = Fund.objects.create(**TEST_FUND_DATA)
        test_fund_2_data = TEST_FUND_DATA.copy()
        test_fund_2_data["name"] = "test2"
        test_fund_2 = Fund.objects.create(**test_fund_2_data)

        expected_fund_data = TEST_FUND_DATA.copy()
        expected_fund_data["id"] = test_fund.id
        expected_fund_2_data = test_fund_2_data.copy()
        expected_fund_2_data["id"] = test_fund_2.id

        response = self.client.get("/funds/")
        expected_response = [expected_fund_data, expected_fund_2_data]
        self.assertEqual(response.json(), expected_response)

    def test_filter_funds_by_strategy(self):
        test_fund = Fund.objects.create(**TEST_FUND_DATA)
        test_fund_2_data = TEST_FUND_DATA.copy()
        test_fund_2_data["name"] = "test2"
        test_fund_2_data["strategy"] = "Global Macro"
        Fund.objects.create(**test_fund_2_data)

        expected_fund_data = TEST_FUND_DATA.copy()
        expected_fund_data["id"] = test_fund.id

        response = self.client.get("/funds/?strategy=Arbitrage")
        expected_response = [expected_fund_data]
        self.assertEqual(response.json(), expected_response)


class GetFundTest(TestCase):
    def test_get_fund_by_id(self):
        test_fund = Fund.objects.create(**TEST_FUND_DATA)
        response = self.client.get(f"/funds/{test_fund.id}/")
        self.assertEqual(response.status_code, 200)

        expected_response = TEST_FUND_DATA.copy()
        expected_response["id"] = test_fund.id
        self.assertDictEqual(response.json(), expected_response)

    def test_returns_404_using_missing_id(self):
        response = self.client.get("/funds/1000/")
        self.assertEqual(response.status_code, 404)


class UploadFundTest(TestCase):
    def test_uses_upload_template(self):
        response = self.client.get("/funds/upload/")
        self.assertTemplateUsed(response, "upload.html")

    def test_uploads_csv_file(self):
        self.assertEqual(Fund.objects.count(), 0)

        csv_data = open("sample_fund_data.csv", "rb")
        csv_file = SimpleUploadedFile(
            content=csv_data.read(), name=csv_data.name, content_type="multipart/form-data"
        )
        data = {"funds_file": csv_file}
        response = self.client.post("/funds/upload/", data, format="multipart")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Fund.objects.count(), 6)


class FundManagerListPage(TestCase):
    def test_uses_list_template(self):
        headers = {"ACCEPT": "text/html"}
        response = self.client.get("/funds/", headers=headers)
        self.assertTemplateUsed(response, "list.html")
