from django.db import models
from django.utils.translation import gettext as _

class Sight(models.Model):
    Longitude  = models.FloatField(
            help_text = _('Longitude of the sight'),)

    Latitude = models.FloatField(
            help_text = _('Latitude of the sight'),)

    Unique_Squirrel_Id = models.CharField(
            help_text = _('The unique ID of the squirrel'),
            max_length = 25,
            )
    
    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES=(
            (AM,'AM'),
            (PM,'PM'),
            )

    Shift = models.CharField(
            help_text = _('Shift of the sight'),
            max_length=16,
            choices=SHIFT_CHOICES,
            blank=True)

    Date = models.DateField(
            help_text = _('Date of the sight in yyyy-mm-dd'),
            null = True,
            blank=True)

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    AGE_CHOICE=(
            (Adult,'Adult'),
            (Juvenile, 'Juvenile'),
            (None, ''),
            )

    Age = models.CharField(
            help_text = _('Age of the squirrel'),
            max_length=16,
            choices = AGE_CHOICE,
            blank = True
            )

    Primary_Fur_Color = models.CharField(
            help_text = _('Fur color'),
            max_length=16,
            blank = True
            )

    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'
    LOCATION_CHOICE=(
            (Ground_Plane, 'Ground Plane'),
            (Above_Ground, 'Above Ground'),
            (None, ''),
            )
    
    Location =  models.CharField(
            help_text = _('Location'),
            max_length=128,
            choices = LOCATION_CHOICE,
            blank = True
            )

    Specific_Location = models.CharField(
            help_text = _('Additional notes to the location'),
            max_length=128,
            blank = True,
            )

    Running = models.BooleanField(
            help_text = _('Running'),
            blank=True,
	    null=True,
    )
    
    Chasing = models.BooleanField(
            help_text = _('Chasing'),
            blank=True,
	    null=True,
    )

    Climbing = models.BooleanField(
            help_text = _('Climbing'),
            blank=True,
	    null=True,
    )

    Eating = models.BooleanField(
            help_text = _('Eating'),
            blank=True,
	    null=True,
    )

    Foraging = models.BooleanField(
            help_text = _('Foraging'),
            blank=True,
	    null=True,
    )

    Other_Activities = models.CharField(
        help_text = _('Other Activities'),
        max_length = 128,
        null = True,
        blank = True
    )

    Kuks = models.BooleanField(
            help_text = _('Kuks'),
            blank=True,
	    null=True,
    )

    Quaas = models.BooleanField(
            help_text = _('Quaas'),
            blank=True,
	    null=True,
    )

    Moans = models.BooleanField(
            help_text = _('Moans'),
            blank=True,
	    null=True,
    )

    Tail_Flags = models.BooleanField(
            help_text = _('Tail_Flags'),
            blank=True,
	    null=True,
    )

    Tail_Twitches = models.BooleanField(
            help_text = _('Tail_Twitches'),
            blank=True,
	    null=True,
    )

    Approaches = models.BooleanField(
            help_text = _('Approaches'),
            blank=True,
	    null=True,
    )

    Indifferent = models.BooleanField(
            help_text = _('Indifferent'),
            blank=True,
	    null=True,
    )
    
    Runs_From = models.BooleanField(
            help_text = _('Runs_From'),
            blank=True,
	    null=True,
    )
