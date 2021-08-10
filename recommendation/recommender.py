import pickle
from dota2web.hero import names, ids
from .filtering import filter_by_roles

antecedents = pickle.load(open("recommendation/antecedents.sav", "rb"))
consequents = pickle.load(open("recommendation/consequents.sav", "rb"))
confidence = pickle.load(open("recommendation/confidence.sav", "rb"))

def getRecommendation(radiant_heroes, dire_heroes):
    """
     Return list of recommendation heroes based on two parameter which are
     list of heroes on radiant and dire team
    """
    # convert heroes name list to id list
    radiant_heroes = convert_heroes_name_to_id(radiant_heroes)
    # print("Radiant heroes id list : %s " % (radiant_heroes))
    dire_heroes = convert_heroes_name_to_id(dire_heroes)
    # print("Dire heroes id list : %s " % (dire_heroes))

    recommended_heroes = []
    total_rules = int(len(antecedents))
    # print("Rules total : %s" % (total_rules))

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

    # recommended_heroes = filter_by_roles(recommended_heroes,radiant_heroes)
    recommended_heroes = convert_heroes_id_to_name(recommended_heroes)
    return recommended_heroes

def convert_heroes_name_to_id(heroes_name):
    """
     Return list of hero id from parameter list of hero name
    """
    heroes_id = []
    for name in heroes_name:
        if name in names:
            idx = names.index(name)
            heroes_id.append(ids[idx])

    return heroes_id

def convert_heroes_id_to_name(heroes_id):
    """
     Return list of hero name from parameter list of hero id
    """
    heroes_name = []
    for id in heroes_id:
        if id in ids:
            idx = ids.index(id)
            heroes_name.append(names[idx])

    return heroes_name
