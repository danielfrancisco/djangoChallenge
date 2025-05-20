from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

def get_data(request):
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
        planetsData = data["data"]["allPlanets"]["planets"]
        
        # for i in planetsData:
        #   Planets.objects.create(**i)
        return JsonResponse({'planets': data})
    else:
        raise Exception(f"GraphQL query failed: {response.status_code}, {response.text}")

      
    
