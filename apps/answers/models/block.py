from django.db.models import Model, JSONField, ForeignKey, CASCADE, DateTimeField

from tests.models import Block
from users.models import User


class AnswerBlock(Model):
    # json
    true_answers = JSONField()
    false_answers = JSONField()
    # date
    created_at = DateTimeField(auto_now_add=True, blank=True)
    # relationship
    block = ForeignKey(Block, CASCADE)
    user = ForeignKey(User, CASCADE)

    @property
    def size(self) -> int:
        return len(self.true_answers) + len(self.false_answers)
