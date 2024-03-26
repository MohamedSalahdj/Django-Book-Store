from rest_framework import pagination


class CustomePageNumberPagination(pagination.PageNumberPagination):
    page_size=12
    max_page_size=12
    page_query_param="page"