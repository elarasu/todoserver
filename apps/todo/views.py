from .models import TodoTask
from rest_framework import viewsets
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todo list to be managed
    """
    queryset = TodoTask.objects.all()
    serializer_class = TodoSerializer
    pagination_class = None
    paginate_by = None

    def perform_create(self, serializer):
        serializer.save(who=self.request.user)

