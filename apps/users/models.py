from django.db.models import Model, CharField, BigIntegerField, DateTimeField


class User(Model):
    first_name = CharField(max_length=150, null=True, blank=True)
    last_name = CharField(max_length=150, null=True, blank=True)
    telegram_id = BigIntegerField(unique=True)

    created_at = DateTimeField(auto_now_add=True, blank=True)
    updated_at = DateTimeField(auto_now=True, null=True, blank=True)
