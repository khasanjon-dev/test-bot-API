from django.db.models import Model, JSONField, ForeignKey, CASCADE, DateTimeField

from tests.models import Block
from users.models import User


class AnswerBlock(Model):
    # json | only save false answers
    mandatory_keys = JSONField()
    first_keys = JSONField()
    second_keys = JSONField()
    # date
    created_at = DateTimeField(auto_now_add=True, blank=True)
    # relationship
    block = ForeignKey(Block, CASCADE)
    user = ForeignKey(User, CASCADE)

    def score(self) -> float:
        return (30 - len(self.mandatory_keys)) * 1.1 + (30 - len(self.first_keys)) * 3.1 + (
                30 - len(self.second_keys)) * 2.1
