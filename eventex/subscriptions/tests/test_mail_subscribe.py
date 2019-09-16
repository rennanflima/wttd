from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValidTest(TestCase):
    def setUp(self):
        data = dict(name='Rennan Lima', cpf='12345678901',
                    email='rennan@lima.net', phone='68-99928-8593')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'rennan@lima.net']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_budy(self):
        contents = [
            'Rennan Lima',
            '12345678901',
            'rennan@lima.net',
            '68-99928-8593',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
    