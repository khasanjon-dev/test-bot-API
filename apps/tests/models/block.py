from django.db.models import Model, CharField, BooleanField, DateTimeField, ForeignKey, CASCADE

from users.models import User


class Block(Model):
    mandatory_keys = CharField(max_length=100)
    first_basic_keys = CharField(max_length=100)
    second_basic_keys = CharField(max_length=100)
    # bool
    is_active = BooleanField(default=True)
    # date
    created_at = DateTimeField(auto_now_add=True, blank=True)
    # relationship
    author = ForeignKey(User, CASCADE, 'blocks')
