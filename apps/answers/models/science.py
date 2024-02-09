from django.db.models import Model, JSONField, DateTimeField, ForeignKey, CASCADE

from tests.models import Science
from users.models import User


class AnswerScience(Model):
    # json | only save false keys
    false_keys = JSONField()
    # date
    created_at = DateTimeField(auto_now_add=True, blank=True)
    # relationship
    science = ForeignKey(Science, CASCADE)
    user = ForeignKey(User, CASCADE)

    @property
    def size(self) -> int:
        return self.science.size

    @property
    def score(self) -> int:
        return self.size - len(self.false_keys)
