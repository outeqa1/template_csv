from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    class Meta:
        db_table = "statuses"

    def __str__(self):
        return self.title

    title = models.CharField(max_length=255, unique=True)


class Record(models.Model):
    class Meta:
        db_table = "records"

    def __str__(self):
        return f"Record status {self.status} from {self.user.username} {self.phone}"

    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=11)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
