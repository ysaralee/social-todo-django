from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import logout

import uuid

# Create your models here.

class TaskManager(models.Manager):
    def create_task(self, owner, title, description):
        task = self.create(owner=owner, title=title, description=description)
        return task

class Task(models.Model):
    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, related_name="owned_tasks")
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    collaborators = models.ManyToManyField(User, related_name="tasks")
    markcomplete = models.BooleanField(default=False)
    isOwnedBy = models.BooleanField(default=True)
    
    objects = TaskManager()

