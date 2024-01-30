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


class AnswerScience(Model):
    keys = CharField(max_length=500)
    true_answers = IntegerField()
    false_answers = IntegerField()
    # relationship
    test = ForeignKey(Science, CASCADE)
    user = ForeignKey(User, CASCADE)
    created_at = DateTimeField(auto_now_add=True, blank=True)


class AnswerBlock(Model):
    keys = CharField(max_length=500)
    true_answers = CharField(max_length=500)
    false_answers = CharField(max_length=500)
    # relationship
    test = ForeignKey(Block, CASCADE)
    user = ForeignKey(User, CASCADE)
    created_at = DateTimeField(auto_now_add=True, blank=True)
