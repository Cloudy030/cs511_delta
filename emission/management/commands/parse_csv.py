import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from emission.models import Country, TotalEmission, PerCapitaEmission, Source

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # Drop the data from the tables to initialise the database, soc we can rerun the files without repitition
        #Country.objects.all().delete()
        #TotalEmission.objects.all().delete()
        PerCapitaEmission.objects.all().delete()
        Source.objects.all().delete()
        print('tables dropped successfully')

        # # Open the csv data files to parse them into the database
        # base_dir = Path(__file__).resolve().parent.parent.parent.parent
        # with open(str(base_dir) + '/data/country.csv', newline='') as f:
        #     reader = csv.reader(f, delimiter=",")
        #     next(reader)    # To skip header line
        #     for row in reader:
        #         print(row)

        #         country = Country.objects.create(
        #             country_name = row[0],
        #             country_code =row[1],
        #         )
        #         country.save()
        # print('Country Table Parsed Successfully')

        # # Open the csv data files to parse them into the database
        # base_dir = Path(__file__).resolve().parent.parent.parent.parent
        # with open(str(base_dir) + '/data/GCB2022v27_MtCO2_flat.csv', newline='') as f:
        #     reader = csv.reader(f, delimiter=",")
        #     next(reader)    # To skip header line
        #     for row in reader:
        #         print(row)

        #         totalemission = TotalEmission.objects.create(
        #             year = int(row[2]),
        #             total = float(row[3]),
        #             coal = float(row[4]),
        #             oil = float(row[5]),
        #             gas = float(row[6]),
        #             cement = float(row[7]),
        #             flaring = float(row[8]),
        #         )
        #         totalemission.save()
        
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/data/GCB2022v27_percapita_flat.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # To skip header line
            for row in reader:
                print(row)

                percapitaemission = PerCapitaEmission.objects.create(
                    year = int(row[2]),
                    percapita = float(row[3]),
                    coal = float(row[4]),
                    oil = float(row[5]),
                    gas =float(row[6]),
                    cement = float(row[7]),
                    flaring = float(row[8]),
                )
                percapitaemission.save()

        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/data/GCB2022v27_sources_flat.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # To skip header line
            for row in reader:
                print(row)

                source = Source.objects.create(
                    coal = row[4],
                    oil = row[5],
                    gas = row[6],
                    cement = row[7],
                    flaring = row[8],
                )
                source.save()

        print("data parsed successfully")