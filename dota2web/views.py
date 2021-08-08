from django.shortcuts import render
from .hero import names, ids

from recommendation.recommender import getRecommendation

def index(request):
    names.sort()

    radiant_heroes = []
    radiant_heroes.append(request.POST.get('inputRadiant1', "empty"))
    radiant_heroes.append(request.POST.get('inputRadiant2', "empty"))
    radiant_heroes.append(request.POST.get('inputRadiant3', "empty"))
    radiant_heroes.append(request.POST.get('inputRadiant4', "empty"))
    radiant_heroes.append(request.POST.get('inputRadiant5', "empty"))
    print("Radiant draft : ", radiant_heroes)

    dire_heroes = []
    dire_heroes.append(request.POST.get('inputDire1', "empty"))
    dire_heroes.append(request.POST.get('inputDire2', "empty"))
    dire_heroes.append(request.POST.get('inputDire3', "empty"))
    dire_heroes.append(request.POST.get('inputDire4', "empty"))
    dire_heroes.append(request.POST.get('inputDire5', "empty"))
    print("Dire draft : ", dire_heroes)

    radiantCounter = request.POST.get('radiantCounter', "1")
    direCounter = request.POST.get('direCounter', "1")

    context = {
        "heroes_name": names,
        "radiant_heroes": radiant_heroes,
        "dire_heroes": dire_heroes,
        "radiantCounter": radiantCounter,
        "direCounter": direCounter,
    }

    if request.method == 'POST':
        # remove empty value from radiant_heroes and dire_heroes
        radiant_heroes = [x for x in radiant_heroes if x != 'empty']
        dire_heroes = [x for x in dire_heroes if x != 'empty']

        if 'recSubmit' in request.POST:
            print("Recommend based on radiant heroes : %s " % (radiant_heroes))
            recommendHeroes = getRecommendation(radiant_heroes, dire_heroes)
            print("List of hero recomendation : %s " % (recommendHeroes))
            context["recommendHeroes"] = recommendHeroes

            return render(request, 'index.html', context)

        if 'predSubmit' in request.POST:
            # if total hero picked for dire and radiant team is not 10 then pass an error
            # else pass prediction result in context
            if len(radiant_heroes) + len(dire_heroes) != 10:
                context["prediction_error_message"] = "Silahkan pilih 5 hero untuk setiap tim."
            else:
                context["predictResult"] = len(dire_heroes) * 100

            return render(request, 'index.html', context)

    return render(request, 'index.html', context)

def simulation(request):
    return render(request, 'simulation.html', {})
