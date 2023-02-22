from rest_framework import viewsets, permissions
from .models import Note
from .serializers import NoteSerializer

# List view
class NoteListView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    allowed_methods = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS')
    permission_classes = [permissions.IsAuthenticated]


# Detail view
class NoteDetailView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Create view
class NoteCreateView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Update view
class NoteUpdateView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Delete view
class NoteDeleteView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Partial update view
class NotePartialUpdateView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
