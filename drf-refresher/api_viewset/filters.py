import django_filters
from .models import Doctors


class DoctorsFilter(django_filters.FilterSet):
    """FilterSet for querying doctors by specialty, name, and ID range."""

    specialty = django_filters.CharFilter(
        field_name="specialty", lookup_expr="icontains"
    )
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    # NOTE: RangeFilter only works on the model's native `id` (IntegerField).
    # For a custom identifier like `doctor_id`, use the id_min/id_max filters below instead.
    # id = django_filters.RangeFilter(field_name='id')

    # Custom min/max filters on `doctor_id`, since it may not be a plain IntegerField.
    # Added label otherwise will display invalid name
    id_min = django_filters.CharFilter(
        method="filter_by_id_range", label="Minimum Doctor ID"
    )
    id_max = django_filters.CharFilter(
        method="filter_by_id_range", label="Maximum Doctor ID"
    )

    class Meta:
        model = Doctors

        fields = ["specialty", "name", "id_min", "id_max"]

    def filter_by_id_range(self, queryset, name, value):
        """Apply a >= or <= filter on doctor_id depending on which bound was passed."""
        if name == "id_min":
            return queryset.filter(doctor_id__gte=value)
        elif name == "id_max":
            return queryset.filter(doctor_id__lte=value)
        return queryset
