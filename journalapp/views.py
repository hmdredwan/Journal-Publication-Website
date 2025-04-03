from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import ResearchPaper
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages

def home(request):
    papers = ResearchPaper.objects.all().order_by('-upload_date')[:6]
    total_papers = ResearchPaper.objects.count()  # Get the total count of papers
    total_authors = ResearchPaper.objects.values('author').distinct().count()  # Count unique authors
    return render(request, 'journal/home.html', {'papers': papers, 'total_papers': total_papers, 'total_authors': total_authors})
    # return render(request, 'journal/home.html', {'papers': papers})

# def publications(request):
#     papers = ResearchPaper.objects.all().order_by('-upload_date')
#     return render(request, 'journal/publications.html', {'papers': papers})

def publications(request):
    query = request.GET.get('search', '')  # Get search query from URL
    if query:
        papers = ResearchPaper.objects.filter(author__icontains=query)  # Filter by author name
    else:
        papers = ResearchPaper.objects.all()  # Show all papers if no search

    return render(request, 'journal/publications.html', {'papers': papers, 'query': query})

def query(request):
    return render(request, 'journal/query.html')

def contact(request):
    return render(request, 'journal/contact.html')

def all_authors(request):
    authors = ResearchPaper.objects.values_list('author', flat=True).distinct()
    return render(request, 'journal/all_authors.html', {'authors': authors})

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            try:
                send_mail(subject, full_message, email, ["your-email@gmail.com"])
                messages.success(request, "Your message has been sent successfully!")
                return redirect("contact")
            except Exception as e:
                messages.error(request, "An error occurred while sending your message. Please try again.")

    else:
        form = ContactForm()

    return render(request, "journal/contact.html", {"form": form})


def query_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"Query from {name}"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(subject, full_message, email, ["your-email@gmail.com"])
            messages.success(request, "Your query has been sent successfully!")
        except Exception as e:
            messages.error(request, "An error occurred while sending your query. Please try again.")

        return redirect("query")  # Redirect back to the query page

    return render(request, "journal/query.html")
