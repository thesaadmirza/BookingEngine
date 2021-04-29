from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """
    Configuring paging rules
    """
    page_size = 12
    page__size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100