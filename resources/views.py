from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse, Http404
from .models import Resource
from .forms import ResourceForm


def resource_list(request):
    """Display all resources with optional subject filtering"""
    resources = Resource.objects.all()
    subject_filter = request.GET.get('subject')

    if subject_filter:
        resources = resources.filter(subject=subject_filter)

    subjects = Resource.SUBJECT_CHOICES

    context = {
        'resources': resources,
        'subjects': subjects,
        'current_subject': subject_filter
    }
    return render(request, 'resources/resource_list.html', context)


@login_required(login_url='/accounts/login/')
def resource_upload(request):
    """Upload a new resource"""
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            # Check file size (max 10MB)
            file = request.FILES['file']
            if file.size > 10 * 1024 * 1024:  # 10MB in bytes
                messages.error(request, 'File size must be less than 10MB')
                return render(request, 'resources/resource_upload.html', {'form': form})

            resource = form.save(commit=False)
            resource.uploader = request.user
            resource.save()
            messages.success(request, 'Resource uploaded successfully!')
            return redirect('resource_list')
    else:
        form = ResourceForm()

    return render(request, 'resources/resource_upload.html', {'form': form})


def resource_download(request, pk):
    """Download a resource file"""
    resource = get_object_or_404(Resource, pk=pk)

    try:
        # Increment download count
        resource.download_count += 1
        resource.save()

        # Serve the file
        response = FileResponse(resource.file.open('rb'))
        response['Content-Disposition'] = f'attachment; filename="{resource.file.name}"'
        return response
    except Exception as e:
        raise Http404("File not found")


def resource_detail(request, pk):
    """Display resource details"""
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, 'resources/resource_detail.html', {'resource': resource})
