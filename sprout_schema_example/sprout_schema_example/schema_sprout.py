from django_schema_sprout.schema_sprout import SchemaSprout

schema_sprout = SchemaSprout("aact")
schema_sprout.create_models(readonly=True)