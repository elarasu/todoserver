from django.db import models
from django.conf import settings
from uuidfield import UUIDField
from django.utils.translation import ugettext_lazy as _

class Task(models.Model):
    uuid = UUIDField(auto=True, hyphenate=False)
    who = models.ForeignKey(settings.AUTH_USER_MODEL)
    task = models.TextField(_("Task"))
    def __unicode__(self):
        return u'%d %s %s %s' % (self.id, self.uuid, self.who, self.task)

# create a Todo Task
class TodoTask(Task):
    """
    A todo task based on Task
    """
    due = models.DateTimeField()
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['-done', 'id']

    def __unicode__(self):
        return u'%d %s %d' % (self.id, self.task, self.done)

