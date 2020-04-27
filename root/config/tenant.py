TENANT_MODEL = "customer.Client"       # app.Model
DEFAULT_FILE_STORAGE = "tenant_schemas.storage.TenantFileSystemStorage"
STATICFILES_STORAGE = "tenant_schemas.storage.TenantStaticFilesStorage"

PUBLIC_SCHEMA_URLCONF = 'root.public_urls'



