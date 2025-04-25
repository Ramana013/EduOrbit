from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from shared.constants import COUNTRY_CODES
from django.apps import apps
# from trainers.models import Qualification, Organization, Awards, Course

def validate_gmail(email):
    if not email.endswith('@gmail.com'):
        raise ValidationError("Email must be a Gmail address.")

# Create your models here.
class Trainer(models.Model):
    IT_EXPERIENCE_CHOICES = [
            ('0-1 years', '0-1 years'),
            ('1-2 years', '1-2 years'),
            ('2-3 years', '2-3 years'),
            ('3-5 years', '3-5 years'),
            ('5-7 years', '5-7 years'),
            ('7-10 years', '7-10 years'),
            ('10+ years', '10+ years'),
            ('Internship', 'Internship'),
            ('Freelancer', 'Freelancer'),
            ('Consultant', 'Consultant'),
            ('Other', 'Other'),
        ]

    QUALIFICATION_CHOICES = [
            ('Bachelor', 'Bachelor'),
            ('Master', 'Master'),
            ('PhD', 'PhD'),
            ('Diploma', 'Diploma'),
            ('Certification', 'Certification'),
            ('Other', 'Other')
        ]

    AWARD_CHOICES = [
            ('Best Trainer', 'Best Trainer'),
            ('Employee of the Year', 'Employee of the Year'),
            ('Outstanding Achievement', 'Outstanding Achievement'),
            ('Certificate of Excellence', 'Certificate of Excellence'),
            ('Best Performance', 'Best Performance'),
            ('Other', 'Other')
        ]

    COURSES_CHOICES = [
            ('Java', 'Java'),
            ('Python', 'Python'),
            ('Django', 'Django'),
            ('Data Science', 'Data Science'),
            ('Machine Learning', 'Machine Learning'),
            ('Other', 'Other')
        ]
    STATUS_CHOICES = [
        (True, 'Active'),
        (False, 'Inactive'),
    ]

    name = models.CharField(max_length=25)
    title = models.CharField(max_length=35)
    bio = models.TextField(max_length=500, verbose_name="Trainer Bio")
    dob = models.DateField(null=True, blank=True)
    training_exp = models.PositiveIntegerField(verbose_name="Training Experience in Years", validators=[MinValueValidator(3), MaxValueValidator(50)], default=3)
    rating = models.DecimalField(
        verbose_name="Rating (1-5)", 
        max_digits=3, 
        decimal_places=1, 
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], default=1.0
    )
    prior_batches = models.PositiveIntegerField(verbose_name="Prior Batches", validators=[MinValueValidator(3), MaxValueValidator(50)], default=3)
    prior_aspirants = models.PositiveIntegerField(verbose_name="Prior Aspirants", validators=[MinValueValidator(3), MaxValueValidator(50)], default=3)
    prior_weekly_tests = models.PositiveIntegerField(verbose_name="Pripor Weekly Tests", validators=[MinValueValidator(3), MaxValueValidator(50)], default=3)
    picture = models.ImageField(upload_to='trainer_pictures/', verbose_name="Trainer Picture",default='trainer_pictures/default.jpg')
    courses_to_train = models.ManyToManyField(
        'Course', 
        blank=True, 
        related_name='trainers', 
        choices=COURSES_CHOICES
    )    # other_courses_to_train = models.CharField(max_length=100, blank=True, null=True, verbose_name="Other Courses")
    
    qualification = models.ManyToManyField('Qualification', blank=True, related_name='qualified_trainers', choices=QUALIFICATION_CHOICES)
    it_exp = models.CharField(
        max_length=20,
        choices=IT_EXPERIENCE_CHOICES,
        verbose_name="IT Experience",
        null=True,
        blank=True,
        default='0-1 years'
    )
    awards = models.CharField(
        max_length=50,
        choices=AWARD_CHOICES,
        verbose_name="Awards",
        null=True,
        blank=True
    )    
    status = models.BooleanField(
        choices=STATUS_CHOICES,
        default=True,
        verbose_name="Status"
    )     # Organization Relationship (One-to-Many)
    # organization = models.ForeignKey(
    #     'Organization',
    #     verbose_name="Organization",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name='trainers',
    #     default="0"  # Default value for organization
    # )
         # Organization Relationship (One-to-Many)
    # awards = models.ForeignKey(
    #     'Awards',
    #     verbose_name="Awards",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name='trainers',
    #     default=" Unknown Award"
    # )

    def __str__(self):
        return f"{self.name} ({self.organization.name if self.organization else 'No Organization'})"
    def __str__(self):
        return f"{self.name} ({self.awards.name if self.awards else 'No Organization'})"
    
    # qualification = models.CharField(max_length=10)
    # college = models.CharField(max_length=30, verbose_name="College/University")
    # experience = models.PositiveIntegerField(verbose_name="IT Experience in Years", validators=[MinValueValidator(3), MaxValueValidator(50)])
    # email = models.EmailField(
    #     max_length=60, 
    #     validators=[validate_gmail],
    #     help_text="This will be used to communicate with trainers officially by administrator")
    # country_code = models.CharField(max_length=3, choices=COUNTRY_CODES, default='+91')

    
    # phone_number = models.CharField(
    #     max_length=10,
    #     validators=[RegexValidator(r'^\d{10}$', 'Mobile number must be exactly 10 digits.')],
    #     help_text='Mobile number will be used to communicate with Trainer by Administrator over WhatsApp',
    # )

    # status = models.BooleanField(default=False)
    def __str__(self):
        return f"Shri. {self.name}, {self.qualification}, {self.experience} yrs experience"
    def save(self, *args, **kwargs):
        super(Trainer, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('trainer_one', kwargs={'pk': self.pk})

class Degree(models.Model):
    title = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    certificate = models.FileField(upload_to='certificates/')

    def __str__(self):
        return self.title
#colleges model
class Colleges(models.Model):
    full_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.full_name

class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    duration_weeks = models.PositiveIntegerField(help_text="Duration of the course in weeks", null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
# Organization Model
class Organization(models.Model):
    STATUS_CHOICES = [
        (True, 'Active'),
        (False, 'Inactive'),
    ]
    
    name = models.CharField(max_length=255, verbose_name="Organization Name", default=0)
    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    short_name = models.CharField(max_length=50, verbose_name="Short Name")
    from_year = models.PositiveIntegerField(
        verbose_name="From Year",
        help_text="The year when the trainer started working in the organization"
    )
    to_year = models.PositiveIntegerField(
        verbose_name="To Year",
        default=0,
        help_text="The ending year of the experience (0 means currently working)"
    )
    
    status = models.BooleanField(
        choices=STATUS_CHOICES,
        default=True,
        verbose_name="Status"
    )

    def __str__(self):
        return self.full_name

# Qualification Model
class Qualification(models.Model):
    STATUS_CHOICES = [
        (True, 'Active'),
        (False, 'Inactive'),
    ]
    
    degree = models.ForeignKey(
        Degree,
        on_delete=models.CASCADE,
        related_name='qualifications'
    )
    college = models.ForeignKey(
        Colleges,  
        on_delete=models.CASCADE,
        related_name='qualifications'
    )
    status = models.BooleanField(
        choices=STATUS_CHOICES,
        default=True,
        verbose_name="Status"
    )

    def __str__(self):
        return f"{self.degree.title} from {self.college.full_name}"

# Awards Model
class Awards(models.Model):
    STATUS_CHOICES = [
        (True, 'Active'),
        (False, 'Inactive'),
    ]
    
    name = models.CharField(max_length=100, blank=True, null=True, default="Unknown Award")  # Add default value here
    full_title = models.CharField(max_length=255, verbose_name="Full Title")
    short_title = models.CharField(max_length=100, verbose_name="Short Title")
    certificate = models.ImageField(
        upload_to='award_certificates/',
        null=True,
        blank=True,
        verbose_name="Certificate"
    )
    status = models.BooleanField(
        choices=STATUS_CHOICES,
        default=True,
        verbose_name="Status"
    )

    def __str__(self):
        return self.short_title