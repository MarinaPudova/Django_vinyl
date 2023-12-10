from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, email=None, password=None, **extra_fields):
        return super().create_user(username, email, password, **extra_fields)
