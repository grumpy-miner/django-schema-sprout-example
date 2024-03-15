from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from sprout_schema_example.schema_sprout import AACT_PUBLIC_SPROUT

schema_view = get_schema_view(
    openapi.Info(
        title="AACT API",
        default_version="1.0.0",
        description="Documentation for the AACT API",
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("api/", include(AACT_PUBLIC_SPROUT.router.urls)),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
