from django.db.models import Model, JSONField, ForeignKey, CASCADE, DateTimeField

from tests.models import Block
from users.models import User


class AnswerBlock(Model):
    # json
    keys = JSONField()
    # date
    created_at = DateTimeField(auto_now_add=True, blank=True)
    # relationship
    block = ForeignKey(Block, CASCADE)
    user = ForeignKey(User, CASCADE)
