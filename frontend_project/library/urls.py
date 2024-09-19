from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import EnrollUserView, ListAvailableBooksView, BorrowBookView

schema_view = get_schema_view(
    openapi.Info(
        title="Library Frontend API",
        default_version='v1',
        description="API documentation for the library frontend service",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mikeinyang975@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('users/enroll/', EnrollUserView.as_view(), name='enroll-user'),
    path('books/', ListAvailableBooksView.as_view(), name='list-books'),
    path('books/<int:id>/borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
