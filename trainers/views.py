from django.shortcuts import get_object_or_404, redirect
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django import forms
from .models import Trainer
from django.urls import reverse_lazy, reverse
from django.views.generic import View, UpdateView, DeleteView, FormView, ListView, DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Degree, Colleges, Organization, Qualification, Awards, Trainer
from .forms import DegreeForm, CollegesForm, OrganizationForm, QualificationForm, AwardForm
from django.shortcuts import render


# create a model form
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        # exclude = ['status']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),  # This line enables the calendar input
        }
    
    def __init__(self, *args, **kwargs):
        super(TrainerForm, self).__init__(*args, **kwargs)
        if 'dob' in self.fields:
            self.fields['dob'].widget.attrs.update({'type': 'date'})
        if 'country_code' in self.fields:
            self.fields['country_code'].disabled = True

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        # If editing an existing trainer (not creating a new one)
        if self.instance and self.instance.pk:
            # Check if the email has been changed
            if email and Trainer.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise ValidationError('A trainer with this email already exists.')
        else:
            # For new trainer creation, ensure the email is unique
            if Trainer.objects.filter(email=email).exists():
                raise ValidationError('A trainer with this email already exists.')

        return email


# Create your views here.
class TrainerFormView(LoginRequiredMixin, FormView):
    form_class = TrainerForm
    template_name = 'trainers/trainer.html' 
    success_url = reverse_lazy('trainers:trainer_view')

    def form_valid(self, form):
        trainer = form.save()
        trainer_name = trainer.name
        messages.success(self.request, f'Trainer "{trainer_name}" created successfully')
        return super().form_valid(form)

# list trainers
class TrainersListView(LoginRequiredMixin, ListView):
    model = Trainer
    context_object_name = 'data'
    template_name = 'trainers/trainers.html'
    ordering = ['-name']

    def post(self, request, *args, **kwargs):
        # Handle the status change when a checkbox is toggled
        trainer_id = request.POST.get('trainer_id')
        trainer = get_object_or_404(Trainer, id=trainer_id)
        trainer.status = not trainer.status  # Toggle the status
        trainer.save()

        # Redirect to the same page after the status is toggled
        return redirect('trainers:trainer_view') 
    
    def get_queryset(self):
        queryset = super().get_queryset().all().order_by('name')
        return queryset

# view each trainer details
class TrainerDetailView(LoginRequiredMixin, DetailView):
    model = Trainer
    template_name = 'trainers/each_trainer.html'
    context_object_name = 'new'

    def get_object(self):
        trainer_id = self.kwargs.get('trainer_id')
        # print(trainer_id)
        try:
            # First try to find by numeric ID
            return Trainer.objects.get(pk=int(trainer_id))
        except (ValueError, Trainer.DoesNotExist):
            # Fall back to searching by name if ID isn't numeric
            return get_object_or_404(Trainer, name=trainer_id)

# remove trainer

class TrainerToggleStatus(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        trainer_id = kwargs.get('trainer_id')
        try:
            # Try numeric ID first
            trainer = Trainer.objects.get(pk=int(trainer_id))
        except (ValueError, Trainer.DoesNotExist):
            # Fall back to name search
            trainer = get_object_or_404(Trainer, name__iexact=trainer_id)
        
        # Rest of your existing logic...
        if trainer.courses_to_train.exists():  # Changed from course_set to courses_to_train
            course_names = ", ".join([course.title for course in trainer.courses_to_train.all()])
            messages.error(request, f'Trainer "{trainer.name}" is assigned to "{course_names}".')
            return redirect('trainers:trainer_view')

        trainer.status = not trainer.status
        trainer.save()
        messages.success(request, f'Status updated for "{trainer.name}"')
        return redirect('trainers:trainer_view')
# class TrainerToggleStatus(LoginRequiredMixin, View):
#     def post(self, request, *args, **kwargs):
#         trainer = Trainer.objects.get(pk=self.kwargs['pk'])  # Fetch the trainer by primary key

#         # Check if the trainer is assigned to any courses
#         if trainer.course_set.exists():
#             course_names = ", ".join([course.title for course in trainer.course_set.all()])
#             messages.error(request, f'Trainer "{trainer.name}" is assigned to "{course_names}". Please untag them from the course(s) to deactivate.')
#             return redirect('trainers:trainer_view')  # Redirect back to the trainer view page

#         # Toggle the status
#         trainer.status = not trainer.status
#         trainer.save()

#         # Send a success message
#         if trainer.status:
#             messages.success(request, f'Trainer "{trainer.name}" has been activated.')
#         else:
#             messages.success(request, f'Trainer "{trainer.name}" has been deactivated.')

#         # Redirect back to the trainer view
#         return redirect('trainers:trainer_view')
    
# edit a trainer

    
class TrainerToggleStatus(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        trainer = Trainer.objects.get(pk=kwargs['pk'])
        
        # Toggle the trainer's status
        if trainer.status:  # If active, trying to deactivate
            if trainer.course_set.exists():  # Check if trainer is assigned to any course
                course_names = ", ".join([course.title for course in trainer.course_set.all()])
                messages.error(self.request, f'Trainer "{trainer.name}" is already assigned to "{course_names}". Please untag them from the course(s) to deactivate.')
                return redirect(reverse('trainers:trainer_view'))  # Redirect back to trainer list
            
            # Deactivate the trainer
            trainer.status = False
            messages.success(self.request, f'Trainer "{trainer.name}" has been deactivated.')
        else:
            # Activate the trainer
            trainer.status = True
            messages.success(self.request, f'Trainer "{trainer.name}" has been activated.')

        trainer.save()
#         return redirect(reverse('trainers:trainer_view'))  # Redirect back to the trainer list after action
def degrees_view(request):
    degrees = Degree.objects.all()
    return render(request, 'trainers/degrees_list.html', {'degrees': degrees})

def add_degree(request):
    if request.method == 'POST':
        form = DegreeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Degree Added Successfully!!")  # <-- Success message
            return redirect('trainers:degrees')
    else:
        form = DegreeForm()
    return render(request, 'trainers/add_degree.html', {'form': form})

# Colleges Views
def colleges_view(request):
    colleges = Colleges.objects.all()
    return render(request, 'trainers/colleges_list.html', {'colleges': colleges})

def add_college(request):
    if request.method == 'POST':
        form = CollegesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "College Added Successfully!!")
            return redirect('trainers:colleges')
    else:
        form = CollegesForm()
    return render(request, 'trainers/add_college.html', {'form': form})

# Organization Views
def organizations_view(request):
    organizations = Organization.objects.all()
    return render(request, 'trainers/organizations_list.html', {'organizations': organizations})

def add_organization(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Organization Added Successfully!!")
            return redirect('trainers:organizations')
    else:
        form = OrganizationForm()
    return render(request, 'trainers/add_organization.html', {'form': form})

# Qualification Views
def qualifications_view(request):
    qualifications = Qualification.objects.all()
    return render(request, 'trainers/qualifications_list.html', {'qualifications': qualifications})

def add_qualification(request):
    if request.method == 'POST':
        form = QualificationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Qualification Added Successfully!!")
            return redirect('trainers:qualifications')
    else:
        form = QualificationForm()
    return render(request, 'trainers/add_qualification.html', {'form': form})

# Awards Views
def awards_view(request):
    awards = Awards.objects.all()
    return render(request, 'trainers/awards_list.html', {'awards': awards})

def add_award(request):
    if request.method == 'POST':
        form = AwardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Award Added Successfully!!")
            return redirect('trainers:awards')
    else:
        form = AwardForm()
    return render(request, 'trainers/add_award.html', {'form': form})

def index_page(request):
    pass

