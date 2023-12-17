from rest_framework import pagination


class RecordPagination(pagination.PageNumberPagination):

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
