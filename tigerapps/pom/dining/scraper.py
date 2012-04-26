

import urllib
from bs4 import BeautifulSoup

#TODO###
dining_halls = {'Wu':2, 'Wilcox':2, 'Rocky':1, 'Mathey':2, 'Forbes':3,
                    'Whitman':8, 'CJL':5, 'Grad College':4}
####

url_stub = 'http://facilities.princeton.edu/dining/_Foodpro/menu.asp?locationNum=0'


class Menu:
    def __init__(self):
        self.meals = []
    def __str__(self):
        return str(self.meals)
    __repr__ = __str__
        
class Meal:
    def __init__(self):
        self.entrees = []
    def __str__(self):
        return str(self.entrees)
    __repr__ = __str__
        
        
class Entree:
    def __init__(self, name='', vegetarian=False, vegan=False, pork=False,
                 nuts=False, earth_friendly=False):
        self.name = name
        self.vegetarian = vegetarian 
        self.vegan = vegan
        self.pork = pork
        self.nuts = nuts
        self.earth_friendly = earth_friendly
    def __str__(self):
        return str(self.__dict__)
    __repr__ = __str__
        

def scrape_single_menu(hall_name):
    """Scrape the menu page for the given dining hall and return the data
    as a menu object"""
    hall_num = dining_halls[hall_name]
    url = url_stub + str(hall_num)
    data = urllib.urlopen(url_stub + str(hall_num)).read()
    bs = BeautifulSoup(data)
    menu = Menu()
    menu.title = bs.title.contents[0]

    for meal_xml in bs.find_all('meal'):
        meal = Meal()
        meal.name = meal_xml.attrs['name']
        for entree_xml in meal_xml.find_all ('entree'):
            entree = Entree()
            entree.name = entree_xml.next.contents[0]
            entree.vegan = True if entree_xml.vegan.contents[0] == 'y' else False
            entree.vegetarian = True if entree_xml.vegetarian.contents[0] == 'y' else False
            entree.pork = True if entree_xml.pork.contents[0] == 'y' else False
            entree.nuts = True if entree_xml.nuts.contents[0] == 'y' else False
            entree.earth_friendly = True if entree_xml.earth_friendly.contents[0] == 'y' else False
            meal.entrees.append(entree)
        menu.meals.append(meal)
    return menu

def scrape_all():
    """Return a list of menus, one for each dining hall"""
    menus = []
    for hall in dining_halls:
        menus.append(scrape_single_menu(hall))
    return menus


