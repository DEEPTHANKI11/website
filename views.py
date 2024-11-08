from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from .models import  Person
from .forms import PersonForm

# Create - Display and handle the form for adding a person
def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')  # Redirect to the list view after creation
    else:
        form = PersonForm()
    return render(request, 'index.html', {'form': form})

# Read - Display all persons
def person_list(request):
    persons = Person.objects.all()
    return render(request, 'index.html', {'persons': persons})

# Update - Show form to update a person's details
def update_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'index.html', {'form': form, 'person': person})

# Delete - Delete a person
def delete_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    return redirect('index.html')