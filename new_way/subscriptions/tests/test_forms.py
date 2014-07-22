# -*- coding: utf-8 -*-
from django.test import TestCase
from new_way.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):

    def test_form_has_fields(self):
        'Form must have 14 fields.'
        form = SubscriptionForm()
        self.assertItemsEqual(
            ['firstname', 'lastname', 'email', 'cpf', 'date_of_birth', 'phone', 'cell', 'address', 'complement',
                'district', 'city', 'uf', 'cep'], form.fields)

    def test_firstname_must_be_capitalized(self):
        'Firstname must be capitalized.'
        form = self.make_validated_form(firstname='REGIS')
        self.assertEqual('Regis', form.cleaned_data['firstname'])

    def test_lastname_must_be_capitalized(self):
        'Lastname must be capitalized.'
        form = self.make_validated_form(lastname='DA SILVA')
        self.assertEqual('Da Silva', form.cleaned_data['lastname'])

    def test_must_inform_email_or_phones(self):
        'Email and Phone are optional, but one must be informed.'
        form = self.make_validated_form(email='', phone='', cell='')
        self.assertItemsEqual(['__all__'], form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(
            firstname='Regis',
            lastname='da Silva',
            cpf='11122233396',
            date_of_birth='1979-05-31',
            email='rg3915@yahoo.com.br',
            phone='11-2600-2500',
            cell='11-98700-0000',
            address=u'Avenida Engenheiro Eusébio Stevaux, 100',
            complement='Bloco A',
            district='Jurubatuba',
            city=u'São Paulo',
            uf='SP',
            cep='04696000'
        )
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
