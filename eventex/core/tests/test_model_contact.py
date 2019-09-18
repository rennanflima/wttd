from django.core.exceptions import ValidationError
from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.core.models import Contact, Speaker


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Rennan Lima',
            slug='rennan-lima',
            photo='https://avatars3.githubusercontent.com/u/7883983?s=460&v=4'
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL,
                                         value='rennan@lima.net')

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE,
                                         value='68-999288593')

        self.assertTrue(Contact.objects.exists())

    def test_choice(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value='rennan@lima.net')
        self.assertEqual('rennan@lima.net', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Rennan Lima',
            slug='rennan-lima',
            photo='https://avatars3.githubusercontent.com/u/7883983?s=460&v=4'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='rennan@lima.net')
        s.contact_set.create(kind=Contact.PHONE, value='68-999288594')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['rennan@lima.net']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['68-999288594']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
