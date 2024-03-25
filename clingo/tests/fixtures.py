# since using pytest-factoryboy here is usually the factory fixture only
import factory
import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from factory.django import DjangoModelFactory
from pytest_factoryboy import register

UserModel = get_user_model()


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Sequence(lambda n: "Group #%s" % n)


class UserFactory(DjangoModelFactory):
    class Meta:
        model = UserModel

    is_superuser = False
    is_staff = True
    username = factory.Sequence(lambda n: f"user_{n}")
    email = factory.LazyAttribute(lambda u: f"{u.username}@example.com")
    password = factory.LazyAttribute(lambda u: make_password(u.username))


register(GroupFactory)  # group, group_factory
register(UserFactory)  # user, user_factory

register(GroupFactory, "admin_group", name="admin")
register(GroupFactory, "sales_group", name="sales")
register(GroupFactory, "operation_group", name="operation")
register(GroupFactory, "supervisor_group", name="supervisor")
register(GroupFactory, "visitor_group", name="visitor")

# register(UserFactory, 'sunny_user', **{
#     'username': 'sunny',
#     'groups': [
#         LazyFixture("supervisor_group"),
#         LazyFixture("operation_group"),
#     ]
# })


@pytest.fixture
def sunny_user(supervisor_group, operation_group):
    # since above register usage for many2many is not working
    # we might as well do it this way
    user = UserFactory.create(username="sunny")
    user.groups.add(supervisor_group, operation_group)
    return user
