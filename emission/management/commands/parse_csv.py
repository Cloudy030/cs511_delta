import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from emission.models import Year, Country, TotalEmission, PerCapitaEmission, Source

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # Drop the data from the tables to initialise the database, soc we can rerun the files without repitition
        Year.objects.all().delete()
        Country.objects.all().delete()
        TotalEmission.objects.all().delete()
        PerCapitaEmission.objects.all().delete()
        Source.objects.all().delete()
        print('tables dropped successfully')

        for i in range(1996,2022):
            year=Year.objects.create(
                year=i
            )
            year.save()
        print('Year Table Parsed Successfully')

        # Open the csv data files to parse them into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/data/country.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)    # To skip header line
            for row in reader:
                print(row)

                country = Country.objects.create(
                    country_name = row[0],
                    #country_code =row[1],
                )
                country.save()
        print('Country Table Parsed Successfully')

        # Open the csv data files to parse them into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/data/GCB2022v27_MtCO2_flat.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)    # To skip header line
            for row in reader:
                print(row)

                # country_id_temp = 0
                # for c in Country.objects.all():
                #     if c.country_name == row[1]:
                #         country_id_temp = c.id
                #         break

                totalemission = TotalEmission.objects.create(
                    country = Country.objects.filter(country_name=row[0]).first(),
                    year = int(row[2]),
                    total = float(row[3]),
                    coal = float(row[4]),
                    oil = float(row[5]),
                    gas = float(row[6]),
                    cement = float(row[7]),
                    flaring = float(row[8]),
                )
                totalemission.save()

        print('TotalEmission Table Parsed Successfully')
        
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/data/GCB2022v27_percapita_flat.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # To skip header line
            for row in reader:
                print(row)

                percapitaemission = PerCapitaEmission.objects.create(
                    country = Country.objects.filter(country_name=row[0]).first(),
                    year = int(row[2]),
                    percapita = float(row[3]),
                    coal = float(row[4]),
                    oil = float(row[5]),
                    gas =float(row[6]),
                    cement = float(row[7]),
                    flaring = float(row[8]),
                )
                percapitaemission.save()

        print('PerCapitaEmission Table Parsed Successfully')

        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/data/GCB2022v27_sources_flat.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # To skip header line
            for row in reader:
                print(row)

                source = Source.objects.create(
                    country = Country.objects.filter(country_name=row[0]).first(),
                    year = int(row[2]),
                    coal = row[4],
                    oil = row[5],
                    gas = row[6],
                    cement = row[7],
                    flaring = row[8],
                )
                source.save()

        print('Source Table Parsed Successfully')

        print("data parsed successfully")