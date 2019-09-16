from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):
    def test_has_action(self):
        """Action mark_as_paid should be installed."""
        model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        self.assertIn('mark_as_paid', model_admin.actions)

    def test_mark_all(self):
        """It should mark all selected subscriptions as paid."""
        Subscription.objects.create(
            name='Rennan Lima',
            cpf='12345678901',
            email='rennan@lima.net',
            phone='68-99928-8593'
        )

        model_admin = SubscriptionModelAdmin(Subscription, admin.site)

        queryset = Subscription.objects.all()
        
        # chamar a actions
        model_admin.mark_as_paid(None, queryset)

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())