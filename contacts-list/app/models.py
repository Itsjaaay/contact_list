from django.db import models
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    is_favorite = models.BooleanField()


def __str__(self):
    self.name, self.email, self.phone, self.is_favorite


def create_contact(name, email, phone, is_favorite):
    contact = Contact(name=name, email=email, phone=phone, is_favorite=is_favorite)
    contact.save()
    return contact


def all_contacts():
    return Contact.objects.all()


def find_contact_by_name(name):
    try:
        contact = Contact.objects.get(name=name)
        return contact
    except ObjectDoesNotExist:
        return None


def favorite_contacts():
    return Contact.objects.filter(is_favorite=True)


def delete_contact(name):
    contact = Contact.objects.get(name=name)
    contact.delete()


def update_contact_email(name, email):
    contact = Contact.objects.get(name=name)
    contact.email = email
    contact.save()