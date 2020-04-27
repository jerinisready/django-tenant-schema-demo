from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
    auto_drop_schema = True





