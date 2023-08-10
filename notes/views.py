from django.shortcuts import render
from django.http import Http404
from django.views.generic import UpdateView, CreateView, DetailView, ListView
from django.views.generic.edit import DeleteView
from .forms import NotesForm
from .models import Notes
# views

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = "notes/notes_delete.html"
    
class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = 'notes/notes_detail.html'