from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email="test@gmail.com", password="test1234"):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        email = "aulia@gmail.com"
        password = "Abc12345"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test the email for a new user is normalized'''
        email = 'test@brainPY.com'
        user = get_user_model().objects.create_user(email, 'test123')
        # check apakah email to lower berhasil
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Create test with no email '''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "1234abcd")

    def test_create_new_superuser(self):
        ''' Test creating a new superusrr '''
        user = get_user_model().objects.create_superuser(
            'test@londonapp.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string represntation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name="Vegan"
        )
        self.assertEqual(str(tag), tag.name)
