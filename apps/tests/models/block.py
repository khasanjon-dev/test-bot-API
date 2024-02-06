from django.db.models import Model, BooleanField, DateTimeField, ForeignKey, CASCADE, JSONField

from users.models import User


class Block(Model):
    # json
    keys = JSONField()
    # bool
    is_active = BooleanField(default=True)
    # date
    created_at = DateTimeField(auto_now_add=True, blank=True)
    # relationship
    author = ForeignKey(User, CASCADE, 'blocks')
