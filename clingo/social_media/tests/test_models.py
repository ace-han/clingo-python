import pytest
from django.contrib.auth.hashers import check_password


@pytest.mark.django_db
@pytest.mark.count_queries(autouse=False)
def test_sunny_user(sunny_user, count_queries):
    assert sunny_user.email == "sunny@example.com"
    assert check_password("sunny", sunny_user.password) is True
    assert sunny_user.groups.filter(name="operation").count() == 1
