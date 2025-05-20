from django.core.management.base import BaseCommand
from datetime import datetime
import requests
from myapp.models import Planets

class Command(BaseCommand):
    help = "Load planets records"

    def handle(self, *args, **kwargs):
        url = "https://swapi-graphql.netlify.app/graphql"
        query = """
        query Query {
        allPlanets {
            planets {
            name
            population
            terrains
            climates
            }
        }
        }
        """
        response = requests.post(url, json={'query': query})

        if response.status_code == 200:
            data = response.json()
            planets_list = data["data"]["allPlanets"]["planets"]
            for planet in planets_list:
                Planets.objects.create(**planet)
            self.stdout.write(self.style.SUCCESS("Planets loaded successfully!"))
        else:
            self.stderr.write("Failed to fetch planets data.")

      