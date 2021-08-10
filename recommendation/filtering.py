from dota2web.hero import ids, roles


roles_count = [
 {'role': 'Carry', 'count': 0},
 {'role': 'Escape', 'count': 0},
 {'role': 'Nuker', 'count': 0},
 {'role': 'Initiator', 'count': 0},
 {'role': 'Durable', 'count': 0},
 {'role': 'Disabler', 'count': 0},
 {'role': 'Jungler', 'count': 0},
 {'role': 'Support', 'count': 0},
 {'role': 'Pusher', 'count': 0}
]

def filter_by_roles(recommended_heroes,radiant_heroes):
    """
    Return a list of hero after filter it by it's roles
    The filtering method used is to remove a hero if there are
    already 3 heroes with the same roles in the radiant
    """

    recommended_heroes_updated = recommended_heroes

    # check for radiant_heroes role
    for hero in radiant_heroes:
        idx  = ids.index(hero)
        radiant_roles = roles[idx]

        for role in radiant_roles:
            add_roles(role)

    # check for recommended_heroes role
    for hero in recommended_heroes:
        idx  = ids.index(hero)
        recommended_roles = roles[idx]

        for role in recommended_roles:
            if not is_role_count_two(role):
                add_roles(role)
            else:
                recommended_heroes_updated.remove(hero)
                break

    return recommended_heroes_updated

def add_roles(role):
    """
    Add role count by one for role in roles_count
    """
    roles_count[0]['count'] += 1 if role == 'Carry' else False
    roles_count[1]['count'] += 1 if role == 'Escape' else False
    roles_count[2]['count'] += 1 if role == 'Nuker' else False
    roles_count[3]['count'] += 1 if role == 'Initiator' else False
    roles_count[4]['count'] += 1 if role == 'Durable' else False
    roles_count[5]['count'] += 1 if role == 'Disabler' else False
    roles_count[6]['count'] += 1 if role == 'Jungler' else False
    roles_count[7]['count'] += 1 if role == 'Support' else False
    roles_count[8]['count'] += 1 if role == 'Pusher' else False

def is_role_count_two(role):
    """
    Return True if the count of the parameter role
    in the role count is 3 else return False
    """
    for role in roles_count:
        if role['count'] == 3:
            return True
    return False
