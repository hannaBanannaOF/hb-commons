from django.shortcuts import get_object_or_404


class QueryStringParamSearchMixin:
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.query_param_fields:
            if field in self.request.query_params: # Ignore empty fields.
                filter[field] = self.request.query_params.get(field)
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj