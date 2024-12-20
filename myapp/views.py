from django.shortcuts import render
from myapp.forms import FeedBackForm

# Create your views here.
def formview(request):
    f = FeedBackForm()  # Create an empty form instance
    if request.method == "POST":
        f = FeedBackForm(request.POST)  # Create form instance with POST data
        if f.is_valid():
            # Safely access cleaned_data with string keys
            name = f.cleaned_data.get('name')  # Default to empty string if not found
            rollno = f.cleaned_data.get('rollno')
            email = f.cleaned_data.get('email')
            FeedBack = f.cleaned_data.get('FeedBack')

            d = {'name': name, 'rollno': rollno, 'email': email, 'FeedBack': FeedBack}
            return render(request, 'htmlpages/output.html', d)

    d = {'forms': f}  # Pass the form instance to the template
    return render(request, 'htmlpages/input.html',d)