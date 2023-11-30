from django.test import TestCase
from .models import Model


# Create your tests here.
class TestModel_test_cases(TestCase):
    def test_Model_creation(self):
        Model1 = Model(title="dog")
        Model1.save()
        self.assertEqual(Model.objects.count(), 1)

    def test_read_all_games(self):
        Model1 = Model.objects.create(title="dog")
        Model1.save()

        Models = Model.objects.all()
        title = [Model.title for Model in Models]
        self.assertEqual(len(title), 1)

    def test_delete_Model(self):
        D = Model(title="dog")
        D.save()

        

        D.delete()
        Models = Model.objects.all()
        self.assertEqual(len(Models), 0)

    def test_update_Model(self):
        Model1 = Model.objects.create(title="dog")
        Model1.save()
        Model1.title = "dog: Black"
        Model1.save()

        self.assertEqual(Model1.title, "dog: Black")

    def test_read_by_title(self):
        Model1 = Model.objects.create(title="dog")
        Model1.save()
        Model_return = Model.objects.get(title="dog")
        self.assertEqual(Model_return.title, "dog")

    def test_filtered_search(self):
        Model1 = Model.objects.create(title="dog")
        Model1.save()
        Model_return = Model.objects.filter(title="dog")
        self.assertEqual(Model_return[0].title, "dog")