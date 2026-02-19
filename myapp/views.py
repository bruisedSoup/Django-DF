from django.shortcuts import render
from django.http import HttpResponse
from .models import Record

def add_record(request):
    new_entry = Record.objects.create(content="This is a test record added via /add")
    return HttpResponse(f"Successfully added: {new_entry.content}")

def show_records(request):
    all_records = Record.objects.all()
  
    output = "<br>".join([r.content for r in all_records])
    return HttpResponse(f"<h1>Stored Records:</h1>{output}")