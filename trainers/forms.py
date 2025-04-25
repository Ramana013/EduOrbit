from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.apps import apps
from django.forms import ModelForm
from django.core.validators import MinValueValidator, MaxValueValidator
# from courseapp.models import Course
from django.db import models


class DegreeForm(forms.ModelForm):
    class Meta:
        from trainers.models import Degree
        model = Degree
        fields = ['title', 'short_name', 'certificate']
class CollegesForm(forms.ModelForm):
    class Meta:
        from .models import Colleges
        model = Colleges
        fields = ['full_name', 'short_name', 'city', 'country', 'status']
class OrganizationForm(forms.ModelForm):
    class Meta:
        from .models import Organization
        model = Organization
        fields = ['full_name', 'short_name', 'from_year', 'to_year', 'status']

class QualificationForm(forms.ModelForm):
    class Meta:
        from.models import Qualification
        model = Qualification
        fields = ['degree', 'college', 'status']

class AwardForm(forms.ModelForm):
    class Meta:
        from .models import Awards
        model = Awards
        fields = ['full_title', 'short_title', 'certificate', 'status']

# Create a model form for Trainer
# class TrainerForm(forms.ModelForm):
#      IT_EXPERIENCE_CHOICES = [
#         ('0-1 years', '0-1 years'),
#         ('1-2 years', '1-2 years'),
#         ('2-3 years', '2-3 years'),
#         ('3-5 years', '3-5 years'),
#         ('5-7 years', '5-7 years'),
#         ('7-10 years', '7-10 years'),
#         ('10+ years', '10+ years'),
#         ('Internship', 'Internship'),
#         ('Freelancer', 'Freelancer'),
#         ('Consultant', 'Consultant'),
#         ('Other', 'Other'),
#     ]

#      QUALIFICATION_CHOICES = [
#         ('Bachelor', 'Bachelor'),
#         ('Master', 'Master'),
#         ('PhD', 'PhD'),
#         ('Diploma', 'Diploma'),
#         ('Certification', 'Certification'),
#         ('Other', 'Other')
#     ]

#      AWARD_CHOICES = [
#         ('Best Trainer', 'Best Trainer'),
#         ('Employee of the Year', 'Employee of the Year'),
#         ('Outstanding Achievement', 'Outstanding Achievement'),
#         ('Certificate of Excellence', 'Certificate of Excellence'),
#         ('Best Performance', 'Best Performance'),
#         ('Other', 'Other')
#     ]

#      COURSES_CHOICES = [
#         ('Java', 'Java'),
#         ('Python', 'Python'),
#         ('Django', 'Django'),
#         ('Data Science', 'Data Science'),
#         ('Machine Learning', 'Machine Learning'),
#         ('Other', 'Other')
#     ]

#      class Meta:
#         model = Trainer
#         fields = [
#             'name', 'title', 'bio', 'dob', 'experience', 'rating', 'profile_pic',
#             'prior_batches', 'prior_aspirants', 'prior_weekly_tests',
#             'courses_to_train', 'qualifications', 'awards', 'it_experience',
#             'email', 'country_code', 'phone', 'status',
#             'other_courses_to_train', 'other_qualifications', 'other_awards'
#         ]
#         widgets = {
#             'courses_to_train': forms.CheckboxSelectMultiple(),
#             'qualifications': forms.CheckboxSelectMultiple(),
#         }

#     # 'Other' fields to be displayed conditionally
#      other_courses_to_train = forms.CharField(
#         required=False,
#         widget=forms.TextInput(attrs={'placeholder': 'Specify Other Courses'}),
#         label="Other Courses (if applicable)"
#     )

#      other_qualifications = forms.CharField(
#         required=False,
#         widget=forms.TextInput(attrs={'placeholder': 'Specify Other Qualifications'}),
#         label="Other Qualifications (if applicable)"
#     )

#      other_awards = forms.CharField(
#         required=False,
#         widget=forms.TextInput(attrs={'placeholder': 'Specify Other Awards'}),
#         label="Other Awards (if applicable)"
#     )

#      it_experience = forms.ChoiceField(
#         choices=IT_EXPERIENCE_CHOICES,
#         label="IT Experience",
#         required=False
#     )

#      def clean(self):
#         cleaned_data = super().clean()

#         # Basic checks
#         if cleaned_data.get('other_courses_to_train') and cleaned_data.get('courses_to_train') == 'Other':
#             if not cleaned_data.get('other_courses_to_train'):
#                 self.add_error('other_courses_to_train', 'Please specify the other course.')

#         if cleaned_data.get('other_qualifications') and cleaned_data.get('qualifications') == 'Other':
#             if not cleaned_data.get('other_qualifications'):
#                 self.add_error('other_qualifications', 'Please specify the other qualification.')

#         if cleaned_data.get('other_awards') and cleaned_data.get('awards') == 'Other':
#             if not cleaned_data.get('other_awards'):
#                 self.add_error('other_awards', 'Please specify the other award.')

#         return cleaned_data
     



# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from captcha.fields import ReCaptchaField
# from .models import CustomUser, UserProfile

# class TrainerRegistrationForm(UserCreationForm):
#     QUALIFICATION_CHOICES = [
#         ('', ''),
#         ('BCA', 'BCA'),
#         ('B.E', 'B.E'),
#         ('B.Sc', 'B.Sc'),
#         ('B.Tech', 'B.Tech'),
#         ('MBA', 'MBA'),
#         ('MCA', 'MCA'),
#         ('M.E', 'M.E'),
#         ('M.Sc', 'M.Sc'),
#         ('M.Tech', 'M.Tech'),
#         ('Ph.D', 'Ph.D'),
#         ('Other', 'Any Other Qualification'),
#     ]

#     EXPERIENCE_CHOICES = [
#         ('', ''),
#         ('0-2 years', '0-2 years'),
#         ('2-5 years', '2-5 years'),
#         ('5-10 years', '5-10 years'),
#         ('10+ years', '10+ years'),
#     ]

#     SPECIALIZATION_CHOICES = [
#         ('', ''),
#         ('Programming', 'Programming'),
#         ('Web Development', 'Web Development'),
#         ('Data Science', 'Data Science'),
#         ('Machine Learning', 'Machine Learning'),
#         ('Cloud Computing', 'Cloud Computing'),
#         ('DevOps', 'DevOps'),
#         ('Cybersecurity', 'Cybersecurity'),
#         ('Database', 'Database'),
#         ('Mobile Development', 'Mobile Development'),
#         ('Other', 'Other'),
#     ]

#     captcha = ReCaptchaField(
#         required=True,
#         label="Captcha *"
#     )

#     first_name = forms.CharField(
#         required=True,
#         max_length=30,
#         label="First Name *",
#         widget=forms.TextInput(attrs={"placeholder": "Enter your first name"})
#     )

#     last_name = forms.CharField(
#         required=True,
#         max_length=30,
#         label="Last Name *",
#         widget=forms.TextInput(attrs={"placeholder": "Enter your last name"})
#     )

#     email = forms.EmailField(
#         required=True,
#         max_length=60,
#         label="Email *",
#         error_messages={
#             'required': 'Email is mandatory.',
#             'invalid': 'Only valid email IDs are accepted for registration.',
#         },
#         help_text="This will be your username for your account."
#     )
    
#     country_code = forms.CharField(
#         required=True,
#         max_length=3,
#         label="Country Code *",
#         widget=forms.TextInput(attrs={"placeholder": "Ex: 091"}),
#         help_text="<br /><br />"
#     )

#     mobile_number = forms.CharField(
#         required=True,
#         max_length=10,
#         label="Mobile Number *",
#         help_text="Should be a 10-digit Mobile number (No '+' required) and will be used for communication."
#     )

#     qualification = forms.ChoiceField(
#         required=True,
#         label="Highest Qualification*",
#         choices=QUALIFICATION_CHOICES,
#     )

#     experience = forms.ChoiceField(
#         required=True,
#         label="Years of Experience*",
#         choices=EXPERIENCE_CHOICES,
#     )

#     specialization = forms.ChoiceField(
#         required=True,
#         label="Primary Specialization*",
#         choices=SPECIALIZATION_CHOICES,
#     )

#     city = forms.CharField(
#         required=True,
#         max_length=30,
#         label="City *"
#     )

#     country = forms.CharField(
#         required=True,
#         max_length=30,
#         label="Country *"
#     )

#     linkedin_profile = forms.URLField(
#         required=False,
#         label="LinkedIn Profile",
#         help_text="Please provide your LinkedIn profile URL (optional)"
#     )

#     github_profile = forms.URLField(
#         required=False,
#         label="GitHub Profile",
#         help_text="Please provide your GitHub profile URL (optional)"
#     )

#     portfolio_website = forms.URLField(
#         required=False,
#         label="Portfolio Website",
#         help_text="Please provide your portfolio website URL (optional)"
#     )

#     password1 = forms.CharField(
#         required=True,
#         label="Password *",
#         widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"}),
#         help_text=(
#             '<ul>'
#             '<li>Your password must contain at least 8 characters.</li>'
#             '<li>Your password can\'t be a commonly used password.</li>'
#             '<li>Your password can\'t be entirely numeric.</li>'
#             '</ul>'
#         ),
#     )
    

#     password2 = forms.CharField(
#         required=True,
#         label="Confirm Password *",
#         widget=forms.PasswordInput(attrs={"placeholder": "Re-enter your password"}),
#         help_text="Re-enter the same password as above for verification.",
#     )

#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'email', 'country_code', 'mobile_number', 
#                  'qualification', 'experience', 'specialization', 'city', 'country',
#                  'linkedin_profile', 'github_profile', 'portfolio_website',
#                  'password1', 'password2', 'captcha']

#         widgets = {
#             'password': forms.PasswordInput(),
#             'country_code': forms.TextInput(),
#         }
#     IT_EXPERIENCE_CHOICES = [
#         ('', '---------'),
#         ('0-1 years', '0-1 years'),
#         ('1-2 years', '1-2 years'),
#         ('2-3 years', '2-3 years'),
#         ('3-5 years', '3-5 years'),
#         ('5-7 years', '5-7 years'),
#         ('7-10 years', '7-10 years'),
#         ('10+ years', '10+ years'),
#         ('Internship', 'Internship'),
#         ('Freelancer', 'Freelancer'),
#         ('Consultant', 'Consultant'),
#         ('Other', 'Other'),
#     ]

#     STATUS_CHOICES = [
#         ('Active', 'Active'),
#         ('Inactive', 'Inactive'),
#         ('On Leave', 'On Leave'),
#     ]

#     # Relationship fields
#     courses_to_train = forms.ModelMultipleChoiceField(
#         queryset=Course.objects.all(),
#         required=False,
#         widget=forms.CheckboxSelectMultiple,  # Or SelectMultiple
#         label='Courses to Train'
#     )

#     qualifications = forms.ModelMultipleChoiceField(
#         queryset=Qualification.objects.all(),
#         required=False,
#         widget=forms.CheckboxSelectMultiple,
#         label='Qualifications'
#     )

#     awards = forms.ModelChoiceField(
#         queryset=Awards.objects.all(),
#         required=False,
#         label='Awards'
#     )

#     IT_EXPERIENCE_CHOICES = [
#     ('0-1 years', '0-1 years'),
#     ('1-2 years', '1-2 years'),
#     ('2-3 years', '2-3 years'),
#     ('3-5 years', '3-5 years'),
#     ('5-7 years', '5-7 years'),
#     ('7-10 years', '7-10 years'),
#     ('10+ years', '10+ years'),
#     ('Internship', 'Internship'),
#     ('Freelancer', 'Freelancer'),
#     ('Consultant', 'Consultant'),
#     ('Other', 'Other'),
# ]

#     it_experience = models.CharField(
#     max_length=100,
#     choices=IT_EXPERIENCE_CHOICES,
#     verbose_name="IT Experience",
#     blank=True,
#     null=True
# )

#     # Other fields
#     other_courses_to_train = forms.CharField(
#         label='Other Courses',
#         required=False
#     )
#     other_qualifications = forms.CharField(
#         label='Other Qualifications',
#         required=False
#     )
#     other_awards = forms.CharField(
#         label='Other Awards',
#         required=False
#     )
#     other_it_experience = forms.CharField(
#         label='Other IT Experience',
#         required=False
#     )

#     class Meta:
#         model = Trainer
#         fields = [
#             'name', 'title', 'bio', 'dob', 'experience', 'rating', 'profile_pic',
#             'prior_batches', 'prior_aspirants', 'prior_weekly_tests',
#             'courses_to_train', 'other_courses_to_train',
#             'qualifications', 'other_qualifications',
#             'awards', 'other_awards',
#             'it_experience', 'other_it_experience',
#             'email', 'country_code', 'phone', 'status'
#         ]

#     def clean(self):
#         cleaned_data = super().clean()

#         # Validate "Other" selections
#         if cleaned_data.get('it_experience') == 'Other' and not cleaned_data.get('other_it_experience'):
#             self.add_error('other_it_experience', 'Please specify the other IT experience.')

#         if not cleaned_data.get('courses_to_train') and not cleaned_data.get('other_courses_to_train'):
#             self.add_error('other_courses_to_train', 'Please select at least one course or specify other.')

#         if not cleaned_data.get('qualifications') and not cleaned_data.get('other_qualifications'):
#             self.add_error('other_qualifications', 'Please select at least one qualification or specify other.')

#         if not cleaned_data.get('awards') and not cleaned_data.get('other_awards'):
#             self.add_error('other_awards', 'Please select an award or specify other.')

#         return cleaned_data

#     IT_EXPERIENCE_CHOICES = [
#         ('', '---------'),
#         ('0-1 years', '0-1 years'),
#         ('1-2 years', '1-2 years'),
#         ('2-3 years', '2-3 years'),
#         ('3-5 years', '3-5 years'),
#         ('5-7 years', '5-7 years'),
#         ('7-10 years', '7-10 years'),
#         ('10+ years', '10+ years'),
#         ('Internship', 'Internship'),
#         ('Freelancer', 'Freelancer'),
#         ('Consultant', 'Consultant'),
#         ('Other', 'Other'),
#     ]

#     COURSES_CHOICES = [
#         ('', '---------'),
#         ('Java', 'Java'),
#         ('Python', 'Python'),
#         ('Django', 'Django'),
#         ('Data Science', 'Data Science'),
#         ('Machine Learning', 'Machine Learning'),
#         ('Other', 'Other'),
#     ]

#     QUALIFICATION_CHOICES = [
#         ('', '---------'),
#         ('Bachelor', 'Bachelor'),
#         ('Master', 'Master'),
#         ('PhD', 'PhD'),
#         ('Diploma', 'Diploma'),
#         ('Certification', 'Certification'),
#         ('Other', 'Other'),
#     ]

#     AWARD_CHOICES = [
#         ('', '---------'),
#         ('Best Trainer', 'Best Trainer'),
#         ('Employee of the Year', 'Employee of the Year'),
#         ('Outstanding Achievement', 'Outstanding Achievement'),
#         ('Certificate of Excellence', 'Certificate of Excellence'),
#         ('Best Performance', 'Best Performance'),
#         ('Other', 'Other'),
#     ]

#     STATUS_CHOICES = [
#         ('Active', 'Active'),
#         ('Inactive', 'Inactive'),
#         ('On Leave', 'On Leave'),
#     ]

#     # Main fields
#     name = forms.CharField(label='Name', required=True)
#     title = forms.CharField(label='Title', required=True)
#     bio = forms.CharField(label='Bio', widget=forms.Textarea, required=True)
#     dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}), required=True)
#     experience = forms.FloatField(label='Experience (years)', required=True)
#     rating = forms.IntegerField(
#         label='Rating (1-5)',
#         validators=[MinValueValidator(1), MaxValueValidator(5)],
#         required=False
#     )
#     profile_pic = forms.ImageField(label='Profile Picture', required=False)
    
#     # Prior experience
#     prior_batches = forms.IntegerField(label='Prior Batches', required=False)
#     prior_aspirants = forms.IntegerField(label='Prior Aspirants', required=False)
#     prior_weekly_tests = forms.IntegerField(label='Prior Weekly Tests', required=False)
    
#     # Choice fields
#     courses_to_train = forms.ChoiceField(
#         label='Courses to Train',
#         choices=COURSES_CHOICES,
#         required=False
#     )
#     qualifications = forms.ChoiceField(
#         label='Qualifications',
#         choices=QUALIFICATION_CHOICES,
#         required=False
#     )
#     awards = forms.ChoiceField(
#         label='Awards',
#         choices=AWARD_CHOICES,
#         required=False
#     )
#     it_experience = forms.ChoiceField(
#         label='IT Experience',
#         choices=IT_EXPERIENCE_CHOICES,
#         required=False
#     )
    
#     # Contact information
#     email = forms.EmailField(label='Email', required=True)
#     country_code = forms.CharField(label='Country Code', required=False)
#     phone = forms.CharField(label='Phone', required=False)
    
#     # Status
#     status = forms.ChoiceField(
#         label='Status',
#         choices=STATUS_CHOICES,
#         required=False
#     )
    
#     # Other fields (will be shown conditionally)
#     other_courses_to_train = forms.CharField(
#         label='Specify Other Courses',
#         required=False,
#         widget=forms.TextInput(attrs={'placeholder': 'Specify Other Courses'})
#     )
#     other_qualifications = forms.CharField(
#         label='Specify Other Qualifications',
#         required=False,
#         widget=forms.TextInput(attrs={'placeholder': 'Specify Other Qualifications'})
#     )
#     other_awards = forms.CharField(
#         label='Specify Other Awards',
#         required=False,
#         widget=forms.TextInput(attrs={'placeholder': 'Specify Other Awards'})
#     )
#     other_it_experience = forms.CharField(
#         label='Specify Other IT Experience',
#         required=False,
#         widget=forms.TextInput(attrs={'placeholder': 'Specify Other IT Experience'})
#     )

#     class Meta:
#         model = Trainer
#         fields = [
#             'name', 'title', 'bio', 'dob', 'experience', 'rating', 'profile_pic',
#             'prior_batches', 'prior_aspirants', 'prior_weekly_tests',
#             'courses_to_train', 'qualifications', 'awards', 'it_experience',
#             'email', 'country_code', 'phone', 'status',
#             'other_courses_to_train', 'other_qualifications', 'other_awards', 'other_it_experience'
#         ]

#     def clean(self):
#         cleaned_data = super().clean()
        
#         # Validate "Other" fields when "Other" is selected
#         if cleaned_data.get('courses_to_train') == 'Other' and not cleaned_data.get('other_courses_to_train'):
#             self.add_error('other_courses_to_train', 'Please specify the other course.')
        
#         if cleaned_data.get('qualifications') == 'Other' and not cleaned_data.get('other_qualifications'):
#             self.add_error('other_qualifications', 'Please specify the other qualification.')
        
#         if cleaned_data.get('awards') == 'Other' and not cleaned_data.get('other_awards'):
#             self.add_error('other_awards', 'Please specify the other award.')
        
#         if cleaned_data.get('it_experience') == 'Other' and not cleaned_data.get('other_it_experience'):
#             self.add_error('other_it_experience', 'Please specify the other IT experience.')
        
#         return cleaned_data     
    

# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import Trainer, Qualification, Organization, Course, ITExperience, Award
# from django.forms import inlineformset_factory

# class TrainerRegistrationForm(UserCreationForm):
#     title = forms.CharField(max_length=100, required=True)
#     bio = forms.CharField(widget=forms.Textarea, required=True)
#     dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
#     training_experience = forms.IntegerField(min_value=0, required=True)
#     rating = forms.FloatField(min_value=1.0, max_value=5.0, required=False)
#     prior_batches = forms.IntegerField(min_value=0, required=True)
#     prior_aspirants = forms.IntegerField(min_value=0, required=True)
#     prior_weekly_tests = forms.IntegerField(min_value=0, required=True)
#     picture = forms.ImageField(required=False)
#     qualifications = forms.ModelMultipleChoiceField(
#         queryset=Qualification.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=False
#     )
#     courses = forms.ModelMultipleChoiceField(
#         queryset=Course.objects.filter(is_active=True),
#         widget=forms.CheckboxSelectMultiple,
#         required=True
#     )

#     class Meta:
#         model = Trainer
#         fields = ['title', 'bio', 'dob', 'training_experience', 'rating',
#                  'prior_batches', 'prior_aspirants', 'prior_weekly_tests',
#                  'picture', 'qualifications', 'courses']

# class ITExperienceForm(forms.ModelForm):
#     class Meta:
#         model = ITExperience
#         fields = ['organization', 'position', 'start_date', 'end_date', 'currently_working', 'description']
#         widgets = {
#             'start_date': forms.DateInput(attrs={'type': 'date'}),
#             'end_date': forms.DateInput(attrs={'type': 'date'}),
#         }

# class AwardForm(forms.ModelForm):
#     class Meta:
#         model = Award
#         fields = ['name', 'awarding_body', 'year_received', 'description']

# ITExperienceFormSet = inlineformset_factory(
#     Trainer, ITExperience, form=ITExperienceForm,
#     extra=1, can_delete=True
# )

# AwardFormSet = inlineformset_factory(
#     Trainer, Award, form=AwardForm,
#     extra=1, can_delete=True
# )
