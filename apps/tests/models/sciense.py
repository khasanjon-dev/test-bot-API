from django.db.models import Model, CharField, JSONField, BooleanField, DateTimeField, ForeignKey, CASCADE

from users.models import User


class Science(Model):
    name = CharField(max_length=150)
    # json
    keys = JSONField()
    # bool
    is_active = BooleanField(default=True)
    # date
    created_at = DateTimeField(auto_now_add=True, blank=True)
    # relationship
    author = ForeignKey(User, CASCADE, 'tests')

    @property
    def size(self) -> int:
        return len(self.keys)
