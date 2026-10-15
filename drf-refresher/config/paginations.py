from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


"""
Custom pagination only works for api function based views and class based views. It does not work for viewsets and generics. 
For viewsets and generics, you need to set the pagination class in the settings.py file.
"""


class CustomPagination(PageNumberPagination):
    page_size = 2  # Number of items per page
    page_query_param = "page_num"  # Allow client to set page size
    max_page_size = 100  # Maximum page size allowed

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "results": data,
            }
        )
