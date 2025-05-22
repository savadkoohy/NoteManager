from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from django.conf import settings
from django.views import View
from django.contrib import messages


# لیست یادداشت‌های کاربر
@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes-apps/note_list.html', {'notes': notes})

# ایجاد یادداشت جدید
@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'یادداشت با موفقیت ایجاد شد!')
            return redirect('notes:note_list')
    else:
        form = NoteForm()
    return render(request, 'notes-apps/note_form.html', {'form': form})

# ویرایش یادداشت
@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes-apps/note_form.html', {'form': form})

# حذف یادداشت
@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes:note_list')
    return render(request, 'notes-apps/note_confirm_delete.html', {'note': note})
