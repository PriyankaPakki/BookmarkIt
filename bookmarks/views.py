from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark
from .forms import BookmarkForm


# 🚪 Signup View
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


# 📋 List Bookmarks
@login_required
def bookmark_list(request):
    bookmarks = Bookmark.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "bookmarks/bookmark_list.html", {"bookmarks": bookmarks})


# ➕ Add Bookmark
@login_required
def bookmark_create(request):
    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            bookmark.save()
            return redirect("bookmark_list")
    else:
        form = BookmarkForm()
    return render(request, "bookmarks/bookmark_form.html", {"form": form})


# ✏️ Edit Bookmark
@login_required
def bookmark_edit(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk, user=request.user)
    if request.method == "POST":
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            form.save()
            return redirect("bookmark_list")
    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, "bookmarks/bookmark_form.html", {"form": form})


# 🗑️ Delete Bookmark
@login_required
def bookmark_delete(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk, user=request.user)
    if request.method == "POST":
        bookmark.delete()
        return redirect("bookmark_list")
    return render(
        request, "bookmarks/bookmark_confirm_delete.html", {"bookmark": bookmark}
    )
