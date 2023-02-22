from django.urls import path
from .views import NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView, NotePartialUpdateView

urlpatterns = [
    path('notes/', NoteListView.as_view(), name='note-list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('notes/create/', NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),  # Update view pattern
    path('notes/<int:pk>/partial-update/', NotePartialUpdateView.as_view(), name='note-partial-update'),
]
