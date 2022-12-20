from django.db import models
from workflow.common.baseModel import BaseModel
from users.models import WorkflowUser
from django.contrib.auth.models import Group
import uuid
# Create your models here.

class AlertScript(BaseModel):
    uniqueId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    alertName = models.CharField(max_length=500)

    def __str__(self):
        return self.alertName


class Workflow(BaseModel):
    uniqueId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    notices = models.CharField(blank=True, max_length=50)
    user = models.ManyToManyField(WorkflowUser, blank=True)
    group = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        return self.name
    
   

class State(BaseModel):
    STATE_CHOICES = (
        ('Start Node', 'Start Node'),
        ('Normal Node', 'Normal Node'),
        ('End Node', 'End Node'),
    )
    uniqueId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    workflow_id = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    stateName = models.CharField(max_length=50, unique=True)
    stateType = models.CharField(max_length=50, choices=STATE_CHOICES)
    group = models.ManyToManyField(Group, blank=True)
    
    def __str__(self):
        return self.stateName


class Transition(BaseModel):
    uniqueId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    workflow_id = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    startState = models.ForeignKey(State,on_delete=models.CASCADE , related_name="transitionsState")
    destinationState = models.ForeignKey(State, on_delete=models.CASCADE,related_name="destinationState")
    conditions = models.CharField(max_length=5000, null=True, blank=True)
    alertMethods = models.ManyToManyField(AlertScript, blank=True)


