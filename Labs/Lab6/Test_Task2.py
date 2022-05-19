import unittest
import Task2
from Task2 import *


class Test_Task2(unittest.TestCase):
    def Test_show_women_Scientist(self):
        sc1 = ["Rosalind", "Franklin", "Notting Hill", "United Kingdom", 1920]
        sci1 = Scientist(sc1)
        makeGreat(sci1, 'helped understand the molecular structures of DNA')
        first_name = sci1.first_name
        last_name = sci1.last_name
        achievement = sci1.achievement
        result = Task2_Method2.show_women_Scientist(first_name, last_name, achievement)
        self.assertEqual(result, 'The Great R. Franklin helped understand the molecular structures of DNA')

        sc2 = ["Marie", "Curie", "Passy", "France", 1934]
        sci2 = Scientist(sc2)
        makeGreat(sci2, 'discovered polonium and radium, championed the use of radiation in medicine and fundamentally changed our understanding of radioactivity')
        first_name = sci2.first_name
        last_name = sci2.last_name
        achievement = sci2.achievement
        result = Task2_Method2.show_women_Scientist(first_name, last_name, achievement)
        self.assertEqual(result, 'The Great M. Curie discovered polonium and radium, championed the use of radiation in medicine and fundamentally changed our understanding of radioactivity')

        sc3 = ["Lise", "Meitner", "Vienna", "Austria", 1878]
        sci3 = Scientist(sc3)
        makeGreat(sci3, 'discovered the element protactinium and nuclear fission')
        first_name = sci3.first_name
        last_name = sci3.last_name
        achievement = sci3.achievement
        result = Task2_Method2.show_women_Scientist(first_name, last_name, achievement)
        self.assertEqual(result, 'The Great L. Meitner discovered the element protactinium and nuclear fission')

        sc4 = ["Katherine", "Johnson", "White Sulphur Springs", "United States", 1918]
        sci4 = Scientist(sc4)
        makeGreat(sci4, 'made calculations of orbital mechanics critical to the success of the first and subsequent NASA crewed spaceflights')
        first_name = sci4.first_name
        last_name = sci4.last_name
        achievement = sci4.achievement
        result = Task2_Method2.show_women_Scientist(first_name, last_name, achievement)
        self.assertEqual(result, 'The Great K. Johnson made calculations of orbital mechanics critical to the success of the first and subsequent NASA crewed spaceflights')

