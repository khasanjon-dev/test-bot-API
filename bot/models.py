from django.db.models import Model, CharField, BigIntegerField, DateTimeField, ForeignKey, CASCADE, BooleanField, \
    IntegerField


class User(Model):
    first_name = CharField(max_length=150, null=True, blank=True)
    last_name = CharField(max_length=150, null=True, blank=True)
    telegram_id = BigIntegerField(unique=True)

    created_at = DateTimeField(auto_now_add=True, blank=True)
    updated_at = DateTimeField(auto_now=True, null=True, blank=True)


class Science(Model):
    name = CharField(max_length=150)
    keys = CharField(max_length=500)
    size = IntegerField()
    # bool
    is_active = BooleanField(default=True)
    # date
    created_at = DateTimeField(auto_now_add=True, blank=True)
    # relationship
    author = ForeignKey(User, CASCADE, 'sciences')


class Answer(Model):
    test = ForeignKey(Science, CASCADE, 'answers')
    user = ForeignKey(User, CASCADE, 'answers')
    keys = CharField(max_length=500)
    true_answers = CharField(max_length=500)
    false_answers = CharField(max_length=500)


class Block(Model):
    keys = CharField(max_length=500)
    size = IntegerField()
    # bool
    is_active = BooleanField(default=True)
    # date
    created_at = DateTimeField(auto_now_add=True, blank=True)
    # relationship
    author = ForeignKey(User, CASCADE, 'blocks')
