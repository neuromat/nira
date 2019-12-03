from django.test import TestCase, RequestFactory

from django.contrib.admin.sites import AdminSite

from custom_auth.admin import CustomUserAdmin
from custom_auth.models import User

USERNAME = "Test_user"
PASSWORD = "Test_psswd"


class CustomUserAdminTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username=USERNAME, password=PASSWORD)
        self.user.is_active = True
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()

        self.factory = RequestFactory()

        self.logged = self.client.login(username=USERNAME, password=PASSWORD)

        self.user1 = User.objects.create_user(username=USERNAME + '0', password=PASSWORD + '0')

    def test_custom_user_admin_returns_the_user_itself_if_it_is_not_superuser(self):
        self.user.is_superuser = False
        self.user.save()
        custom_user_admin = CustomUserAdmin(User, AdminSite())

        qs = custom_user_admin.get_queryset(self)
        self.assertEqual(list(qs), [self.user])

    def test_custom_user_admin_returns_all_users_if_it_is_not_superuser(self):
        custom_user_admin = CustomUserAdmin(User, AdminSite())

        qs = custom_user_admin.get_queryset(self)
        self.assertIn(self.user1, qs)
        self.assertIn(self.user, qs)

    def test_get_fieldsets_when_superuser(self):
        custom_user_admin = CustomUserAdmin(User, AdminSite())
        fields = custom_user_admin.get_fieldsets(self)

        fields_expected = [(None, {'fields': ('username', 'password1', 'password2')})]
        self.assertEqual(list(fields), fields_expected)

    def test_get_fieldsets_when_not_superuser(self):
        self.user.is_superuser = False
        self.user.save()
        custom_user_admin = CustomUserAdmin(User, AdminSite())
        fields = custom_user_admin.get_fieldsets(self)

        fields_expected = [(None, {'fields': ('username', 'password')})]
        self.assertEqual(list(fields), fields_expected)
