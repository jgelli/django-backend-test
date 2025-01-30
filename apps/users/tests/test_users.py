import json
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase