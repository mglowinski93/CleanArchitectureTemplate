from uuid import uuid4, UUID

import factory
from faker import Faker

from apps.template_app.domain.entities import Template
from utils import get_current_utc_timestamp


fake = Faker()


class TemplateFactory(factory.Factory):
    class Meta:
        model = Template

    id = factory.LazyFunction(uuid4)
    value = factory.Faker("sentence")
    timestamp = factory.LazyFunction(get_current_utc_timestamp)


def fake_template_id() -> UUID:
    return uuid4()


def fake_template_value() -> str:
    return fake.pystr(min_chars=1, max_chars=100)
