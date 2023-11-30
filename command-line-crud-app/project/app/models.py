from django.db import models


# Create your models here.
class Model(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


# create game
def make_Model(title):
    Model1 = Model(title=title)
    Model1.save()


# read all
def read_all_Models():
    return Model.objects.all()


# read filtered
def Model_filter(title):
    return Model.objects.filter(title=title)


# reads by unique identifier(title)
def read_by_title(title):
    return Model.objects.get(title=title)


# updates Model name
def update_Model(old_title, new_title):
    Model = Model.objects.get(title=old_title)
    Model.title = new_title
    Model.save()


# deletes game
def delete_Model(title):
    D = Model.objects.filter(title=title)
    D.delete()