from django.db.models import Model, JSONField, ForeignKey, CASCADE, DateTimeField

from tests.models import Block
from users.models import User


class AnswerBlock(Model):
    # json
    mandatory_keys_true = JSONField(max_length=30)
    mandatory_keys_false = JSONField(max_length=30)
    first_keys_true = JSONField(max_length=30)
    first_keys_false = JSONField(max_length=30)
    second_keys_true = JSONField(max_length=30)
    second_keys_false = JSONField(max_length=30)

    # date
    created_at = DateTimeField(auto_now_add=True, blank=True)
    # relationship
    block = ForeignKey(Block, CASCADE)
    user = ForeignKey(User, CASCADE)
