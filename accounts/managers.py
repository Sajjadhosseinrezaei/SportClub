from django.contrib.auth.models import BaseUserManager as BM


class UserManager(BM):
    def create_user(self, name, email, password=None):
        user = self.model(name=name, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
