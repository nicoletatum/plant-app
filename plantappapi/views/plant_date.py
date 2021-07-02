from datetime import date

from rest_framework.viewsets import ViewSet

class DateView(ViewSet):

    def retrieve(self, request):    
        today = date.today()

        # https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-date-based/
        # https://docs.python.org/3/library/datetime.html?highlight=date