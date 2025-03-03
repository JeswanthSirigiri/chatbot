# from django.db import models
#
# class Query(models.Model):
#     question = models.TextField()
#     response = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
# # Create your models here.
#
from django.db import models

class Query(models.Model):
    question = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Q: {self.question} | A: {self.response}"
        # return f"Query: {self.question[:50]}"
