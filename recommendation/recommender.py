import pickle
from dota2web.hero import names, ids

antecedents = pickle.load(open("recommendation/antecedents.sav", "rb"))
consequents = pickle.load(open("recommendation/consequents.sav", "rb"))
confidence = pickle.load(open("recommendation/confidence.sav", "rb"))

def getRecommendation(radiant_heroes, dire_heroes):
    """
     Return list of recomendation heroes based on two parameter which are
     list of heroes on radiant and dire team
    """
    # convert heroes name list to id list
    radiant_heroes = getHeroesId(radiant_heroes)
    print("Radiant heroes id list : %s " % (radiant_heroes))
    dire_heroes = getHeroesId(dire_heroes)
    print("Dire heroes id list : %s " % (dire_heroes))

    recommended_heroes = []
    total_rules = int(len(antecedents))
    print("Rules total : %s" % (total_rules))

    # recommend based on every hero on radiant team
    for hero in radiant_heroes:
        for i in range(total_rules):
            if hero in antecedents[i]:
                # add every hero in consequents that not in radiant or dire team
                # to recommendation list and make sure there are no duplicates
                for cons_hero in consequents[i]:
                    if cons_hero not in recommended_heroes:
                        if cons_hero not in radiant_heroes:
                            if cons_hero not in dire_heroes:
                                recommended_heroes.append(cons_hero)

    recommended_heroes = getHeroesName(recommended_heroes)
    return recommended_heroes

def getHeroesId(hero_names):
    """
     Return list of hero id from parameter list of hero name
    """
    hero_ids = []
    for name in hero_names:
        idx = names.index(name)
        hero_ids.append(ids[idx])

    return hero_ids

def getHeroesName(hero_ids):
    """
     Return list of hero name from parameter list of hero id
    """
    hero_names = []
    for id in hero_ids:
        idx = ids.index(id)
        hero_names.append(names[idx])

    return hero_names
