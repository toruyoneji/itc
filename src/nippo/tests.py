from django.test import TestCase
from .models import NippoModel
from django.urls import reverse


class NippoTestCase(TestCase):
    def setUp(self):
       obj = NippoModel(title="titleTest1", content="contentTest1")
       obj.save()

#データが正しく保存されているか
    def test_saved_single_object(self):
        qs_counter = NippoModel.objects.count()
        self.assertEqual(qs_counter, 1)

#404ページが返ってくるか
    def test_response_404(self):
        detail_url = reverse('nippo-detail', kwargs={"pk": 100})
        detail_response = self.client.get(detail_url)
        update_url = reverse('nippo-update', kwargs={"pk": 100})
        update_response = self.client.get(update_url)
        delete_url = reverse('nippo-delete', kwargs={"pk": 100})
        delete_response = self.client.get(delete_url)
        self.assertEqual(detail_response.status_code, 404)
        self.assertEqual(update_response.status_code, 404)
        self.assertEqual(delete_response.status_code, 404)

#createページできちんとデータが保存されているか
    def test_create_on_createView(self):
        url = reverse('nippo-create')
        create_data = {"title": "title_from_test", "content": "content_from_test"}
        response = self.client.post(url, create_data)
        qs_counter2 = NippoModel.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(qs_counter2, 2)

    # def test_listview_with_anonymous(self):
    #     url = reverse("nippo-list")
    #     response = self.client.get(url)
    #     object_list = response.context_data["object_list"]
    #     self.assertEqual(len(object_list), 0)

    # def test_listview_with_own_user(self):
    #     url = reverse("nippo-list")
    #     self.client.login(email=self.email, password=self.password)
    #     response = self.client.get(url)
    #     object_list = response.context_data["object_list"]
    #     self.assertEqual(len(object_list), 1)

    # def test_slug_saved(self):
    #     nippo_obj = NippoModel.objects.first()
    #     self.assertTrue(nippo_obj.slug)