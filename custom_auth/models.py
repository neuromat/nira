from django.db import models
from django.utils.translation import ugettext_lazy as _
import re
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from person.models import Person


class UserManager(BaseUserManager):

    def _create_user(self, username, password, is_staff, is_superuser):
        """
        Creates and saves a User with the given username and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))

        user = self.model(username=username, is_staff=is_staff, is_active=False, is_superuser=is_superuser,
                          last_login=now, date_joined=now)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None):
        user = self._create_user(username, password, False, False)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self._create_user(username, password, True, True)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Username'), max_length=30, unique=True,
                                help_text=_('Required. 30 characters or fewer. '
                                            'Letters, numbers and @/./+/-/_ characters'),
                                validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                                      _('Enter a valid username.'), _('invalid'))])
    is_staff = models.BooleanField(_('Staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('Active'), default=False,
                                    help_text=_('Designates whether this user should be treated as active. '
                                                'Unselect this instead of deleting accounts.'))
    is_nira_admin = models.BooleanField(_('NIRA admin'), default=False,
                                        help_text=_('Designates whether the user can create content on behalf of '
                                                    'another user.'))
    force_password_change = models.BooleanField(_('Force password change'), default=True,
                                                help_text=_('Force the user to change their password at next login.'))
    date_joined = models.DateTimeField(_('Date joined'), default=timezone.now)
    user_profile = models.OneToOneField(Person, verbose_name=_('User profile'), blank=True, null=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    # Returns the username
    def __unicode__(self):
        return self.username

    # Used at welcome message.
    def get_short_name(self):
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')