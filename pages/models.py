from django.db import models
from django.contrib.auth.models import User

class House(models.Model):
    REGIONS = [

        ('Arusha','Arusha'),

        ('Dar es Salaam ','Dar es Salaam'),

        ('Dodoma','Dodoma') ,

        ('Geita','Geita'),

        ('Iringa','Iringa'),

        ('Kagera','Kagera'),

        ('Katavi','Katavi'),

        ('Kigoma','Kigoma'),

        ('Kilimanjaro','Kilimanjaro'), 

        ('Lindi','Lindi'), 

        ('Manyara','Manyara'), 

        ('Mara','Mara'), 

        ('Mbeya','Mbeya'),

        ('Zanzibar','Zanzibar'), 

        ('Morogoro','Morogoro'), 

        ('Mtwara','Mtwara'),

        ('Mwanza','Mwanza'), 

        ('Njombe','Njombe'), 

        ('Pemba North','Pemba North'),

        ('Pemba South','Pemba South'),

        ('Pwani','Pwani'), 

        ('Rukwa','Rukwa'), 

        ('Ruvuma','Ruvuma'),

        ('Shinyanga','Shinyanga'), 

        ('Simiyu','Simiyu'), 

        ('Singida','Singida'), 

        ('Songwe','Songwe'), 

        ('Tabora','Tabora'), 

        ('Tanga','Tanga'), 

    ]

    owners_name = models.CharField(max_length=100,null=False,blank=False)
    owners_phone_1 = models.CharField(max_length=15, help_text="+255 format",null=False,blank=False)
    owners_phone_2 = models.CharField(max_length=15, help_text="+255 format",null=False,blank=False)
    house_owner = models.CharField(max_length=100,null=False,blank=False)
    number_of_rooms = models.PositiveIntegerField(default=0,null=False,blank=False)
    price_per_day = models.PositiveIntegerField(default=0,null=False,blank=False)
    minimum_booking_per_day = models.PositiveIntegerField(default=0,null=False,blank=False)
    instructions = models.TextField(null=False,blank=False)
    description = models.TextField(null=False,blank=False)
    region = models.CharField(max_length=100, choices=REGIONS,null=False,blank=False)
    district = models.CharField(max_length=100,null=False,blank=False)
    street_name = models.CharField(max_length=100,null=False,blank=False)
    house_number = models.PositiveIntegerField(default=0,null=False,blank=False)
    google_map = models.CharField(max_length=100,null=False,blank=False)
    ametuer = models.CharField(max_length=100,null=False,blank=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owners_name
    




