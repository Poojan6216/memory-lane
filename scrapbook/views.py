from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Memory, SharedAccess
from .forms import MemoryForm
from django.core.paginator import Paginator


@login_required
def timeline(request):
    #memories = Memory.objects.filter(user=request.user).order_by('-created_at')
    personal_memories = Memory.objects.filter(user=request.user).order_by('-created_at')

    shared_memories = Memory.objects.filter(
    id__in=SharedAccess.objects.filter(shared_with=request.user).values_list('memory_id', flat=True)
    )

    # Combine personal and shared memories
    all_memories = (personal_memories | shared_memories).distinct().order_by('-created_at')

    # Add pagination (5 memories per page)
    paginator = Paginator(all_memories, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #shared_memories = Memory.objects.filter(
    #id__in=SharedAccess.objects.filter(shared_with=request.user).values_list('memory_id', flat=True)
    #)
    return render(request, 'scrapbook/timeline.html', {'page_obj':page_obj })

@login_required
def add_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.save()
            form.save_m2m()  # Save the Many-to-Many relationships

            # Populate SharedAccess table
            shared_users = form.cleaned_data['shared_with']
            for user in shared_users:
                SharedAccess.objects.create(memory=memory, shared_with=user)

            return redirect('timeline')
    else:
        form = MemoryForm()
    return render(request, 'scrapbook/add_memory.html', {'form': form})


@login_required
def memory_detail(request, memory_id):
    memory = get_object_or_404(Memory, id=memory_id, user=request.user)
    return render(request, 'scrapbook/memory_detail.html', {'memory': memory})

@login_required
def my_memories(request):
    user_memories = Memory.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(user_memories, 5)  # Show 5 memories per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'scrapbook/my_memories.html', {'page_obj': page_obj})

@login_required
def edit_memory(request, pk):
    memory = get_object_or_404(Memory, id=pk, user=request.user)
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES, instance=memory)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.save()
            form.save_m2m()  # Save Many-to-Many relationships

            # Update SharedAccess table
            SharedAccess.objects.filter(memory=memory).delete()  # Remove old shared data
            shared_users = form.cleaned_data['shared_with']
            for user in shared_users:
                SharedAccess.objects.create(memory=memory, shared_with=user)

            return redirect('my_memory')
    else:
        form = MemoryForm(instance=memory)
    return render(request, 'scrapbook/edit_memory.html', {'form': form, 'memory': memory})


@login_required
def delete_memory(request, pk):
    memory = get_object_or_404(Memory, id=pk, user=request.user)
    memory.delete()
    #return redirect('my_memories')
    return redirect('my_memory')
