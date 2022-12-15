from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Portfolio

class PortfolioTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        cls.post = Portfolio.objects.create(
            caption="A good title",
        )