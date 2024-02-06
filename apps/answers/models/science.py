from django.db.models import Model, JSONField, DateTimeField, ForeignKey, CASCADE

from tests.models import Science
from users.models import User


class AnswerScience(Model):
    # json
    true_answers = JSONField()
    false_answers = JSONField()
    # date
    created_at = DateTimeField(auto_now_add=True, blank=True)
    # relationship
    science = ForeignKey(Science, CASCADE)
    user = ForeignKey(User, CASCADE)

    @property
    def size(self) -> int:
        return len(self.true_answers) + len(self.false_answers)
