from django.test import TestCase
from .models import Model


# Create your tests here.
class TestModel_test_cases(TestCase):
    def test_Model_creation(self):
        Model = Model(title="Pokemon")
        Model.save()
        self.assertEqual(Model.objects.count(), 1)

    def test_read_all_games(self):
        Model = Model.objects.create(title="Pokemon")
        Model.save()

        Models = Model.objects.all()
        title = [Model.title for Model in Models]
        self.assertEqual(len(title), 1)

    def test_delete_Model(self):
        D = Model(title="Pokemon")
        D.save()

        # title = [Model.title for Model in Models]

        D.delete()
        Models = Model.objects.all()
        self.assertEqual(len(Models), 0)

    def test_update_Model(self):
        Model = Model.objects.create(title="Pokemon")
        Model.save()
        Model.title = "Pokemon: Black"
        Model.save()

        self.assertEqual(Model.title, "Pokemon: Black")

    def test_read_by_title(self):
        Model = Model.objects.create(title="Pokemon")
        Model.save()
        Model_return = Model.objects.get(title="Pokemon")
        self.assertEqual(Model_return.title, "Pokemon")

    def test_filtered_search(self):
        Model = Model.objects.create(title="Pokemon")
        Model.save()
        Model_return = Model.objects.filter(title="Pokemon")
        self.assertEqual(Model_return[0].title, "Pokemon")