from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    text = models.TextField()

    created_by = models.ForeignKey(
        User,
        null = True,
        on_delete = models.SET_NULL
    )

    created_at = models.DateTimeField(
        auto_now_add = True,
    )

    updated_at = models.DateTimeField(
        auto_now = True
    )

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.pk} - {self.text[:25]}"
