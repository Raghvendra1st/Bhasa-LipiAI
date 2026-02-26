from django.shortcuts import render
from .forms import DocumentForm
from .utils import extract_text, translate_text

def upload_document(request):
    extracted_text = None
    translated_text = None

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            file_path = document.file.path

            # Extract English text
            extracted_text = extract_text(file_path)

            # Translate to Hindi
            translated_text = translate_text(extracted_text)
    else:
        form = DocumentForm()

    return render(request, 'lipi/upload.html', {
        'form': form,
        'extracted_text': extracted_text,
        'translated_text': translated_text
    })
