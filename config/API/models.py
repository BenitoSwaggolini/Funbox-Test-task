from django.db import models


class Link(models.Model):
    link = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link

    def __eq__(self, obj):
        return self.link == obj.link
