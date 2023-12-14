from django.db.models import Model, CharField, BigIntegerField, DateTimeField, IntegerField, ForeignKey, CASCADE, \
    BooleanField


class User(Model):
    first_name = CharField(max_length=150, null=True, blank=True)
    last_name = CharField(max_length=150, null=True, blank=True)
    telegram_id = BigIntegerField(unique=True)

    created_at = DateTimeField(auto_now_add=True, blank=True)
    updated_at = DateTimeField(auto_now=True, null=True, blank=True)


class Science(Model):
    name = CharField(max_length=150)
    size = IntegerField()
    keys = CharField(max_length=250)
    # boolean
    is_active = BooleanField(default=True)
    # date
    created_at = DateTimeField(auto_now_add=True, blank=True)
    # relationship
    author = ForeignKey(User, CASCADE, 'sciences')


class CheckTestAnswers(Model):
    test_id = ForeignKey(Science, CASCADE, 'answers')


class Block(Model):
    name = CharField(max_length=150, default='Blok Test')
    size = IntegerField()
    keys = CharField(max_length=250)
    # boolean
    is_active = BooleanField(default=True)
    # date
    created_at = DateTimeField(auto_now_add=True, blank=True)
    # relationship
    author = ForeignKey(User, CASCADE, 'blocks')
