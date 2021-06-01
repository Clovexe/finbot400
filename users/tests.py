from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class costumer_test(TestCase):
    def test_new_supeuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'test@gmail.com','username', 'abcec', 'absas','1213434'
        )
        self.assertEqual(super_user.email,'test@gmail.com')
