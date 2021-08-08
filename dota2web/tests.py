from django.test import TestCase

from recommendation.recommender import getRecommendation

class RecommenderTestCase(TestCase):

    def test_getrecommendation_not_return_duplicate(self):
        """
        getRecommendation will not return duplicate result
        even if it given duplicate heroes on input radiant team
        """
        teamA = ['Bloodseeker','Bloodseeker','Bloodseeker']
        teamB = ['Anti-Mage','Axe']
        recommended_heroes = getRecommendation(teamA, teamB)

        # checking duplicate
        for x in set(recommended_heroes):
            recommended_heroes.remove(x)
        duplicate = list(set(recommended_heroes))

        duplicate = len(duplicate)
        self.assertIs(duplicate, 0)

        
