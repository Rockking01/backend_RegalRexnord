from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
      
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
       
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    birthday = models.DateField(null=True)
    is_manager = models.BooleanField(default=False)
    USERNAME_FIELD = "email"

    objects = UserManager()

    @property
    def total_score(self):
        from .scoreboad import Scoreboard
        scores = Scoreboard.objects.all().filter(user=self)
        total = 0
        for score in scores:
            total = total + score.score
        
        return total

    @property
    def average_score(self):
        from .scoreboad import Scoreboard
        scores = Scoreboard.objects.all().filter(user=self)
        if (len(scores) == 0):
            return 0
        return self.total_score / len(scores)


