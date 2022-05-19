class Scientist:
    def __init__(self, list):
        self.first_name = list[0]
        self.last_name = list[1]
        self.city = list[2]
        self.COB = list[3]
        self.YOB = list[4]
        self.achievement = ''

    def displayScientist(self):
        print(f'City: {self.city}\nCountry of Birth: {self.COB}\nYear of Birth: {self.YOB}\n')


def makeGreat(sci, achievement):
    sci.achievement = achievement
    sci.first_name = f'The Great {sci.first_name[0]}.'

def show_women_Scientist(sci):
    return f'{sci.first_name} {sci.last_name} {sci.achievement}'

def test_show_women_Scientist():
    assert show_women_Scientist(sci1) == 'The Great R. Franklin helped understand the molecular structures of DNA', 'Should be The Great R. Franklin helped understand the molecular structures of DNA'
    assert show_women_Scientist(sci2) == 'The Great M. Curie discovered polonium and radium, championed the use of radiation in medicine and fundamentally changed our understanding of radioactivity', 'Should be The Great M. Curie discovered polonium and radium, championed the use of radiation in medicine and fundamentally changed our understanding of radioactivity'
    assert show_women_Scientist(sci3) == 'The Great L. Meitner discovered the element protactinium and nuclear fission', 'Should be The Great L. Meitner discovered the element protactinium and nuclear fission'
    assert show_women_Scientist(sci4) == 'The Great K. Johnson made calculations of orbital mechanics critical to the success of the first and subsequent NASA crewed spaceflights', 'Should be The Great K. Johnson made calculations of orbital mechanics critical to the success of the first and subsequent NASA crewed spaceflights'




if __name__ == '__main__':

    sc1 = ["Rosalind","Franklin","Notting Hill","United Kingdom",1920]
    sc2 = ["Marie","Curie","Passy","France",1934]
    sc3 = ["Lise","Meitner","Vienna","Austria",1878]
    sc4 = ["Katherine","Johnson","White Sulphur Springs","United States",1918]

    sci1 = Scientist(sc1)
    sci2 = Scientist(sc2)
    sci3 = Scientist(sc3)
    sci4 = Scientist(sc4)

    list_of_sci = [sci1, sci2, sci3, sci4]

    for sci in list_of_sci:
        print(f'{sci.first_name} {sci.last_name}:')
        sci.displayScientist()

    makeGreat(sci1,'helped understand the molecular structures of DNA')
    makeGreat(sci2, 'discovered polonium and radium, championed the use of radiation in medicine and fundamentally changed our understanding of radioactivity')
    makeGreat(sci3, 'discovered the element protactinium and nuclear fission')
    makeGreat(sci4,'made calculations of orbital mechanics critical to the success of the first and subsequent NASA crewed spaceflights')

    for sci in list_of_sci:
        print(show_women_Scientist(sci))

    test_show_women_Scientist()
    print('\nPass Test')