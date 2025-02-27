from data import CountyDemographics

#Part 1
def population_total(lst: list[CountyDemographics]) -> int:
    pop_total = 0
    for num in lst:
        pop_total += num.population.get('2014 Population')

    return pop_total

#Part 2
def filter_by_state(lst: list[CountyDemographics], state: str) :
    filter_list = []
    for name in lst:
        if name.state == state:
            filter_list.append(name)

    return filter_list

#Part3
def population_by_education(lst: list[CountyDemographics], ed_key: str):
    ed_total = 0
    for num in lst:
        if num.education.get(ed_key):
            per = num.education.get(ed_key)/100
            ed_total += num.population.get("2014 Population") * per
    return ed_total

def population_by_ethnicity(lst: list[CountyDemographics], eth:str):
    eth_total = 0
    for num in lst:
        if num.ethnicities.get(eth):
            per = num.ethnicities.get(eth) / 100
            eth_total += num.population.get("2014 Population") * per
    return eth_total

def population_below_poverty_level(lst: list[CountyDemographics]):
    pov_total = 0
    for num in lst:
        per = num.income.get("Persons Below Poverty Level") / 100
        pov_total += num.population.get('2014 Population') * per

    return pov_total

#Part4
def percent_by_education(lst: list[CountyDemographics], perc: str):
    per_total = population_total(lst)
    ed_total = population_by_education(lst,perc)
    try:
        ed_percent = ed_total/per_total
    except ZeroDivisionError:
        ed_percent = 0.0
    return ed_percent*100

def percent_by_ethnicity(lst: list[CountyDemographics], perc: str):
    per_total = population_total(lst)
    eth_total = population_by_ethnicity(lst, perc)
    try:
        ed_percent = eth_total / per_total
    except ZeroDivisionError:
        ed_percent = 0.0
    return ed_percent * 100

def percent_below_poverty_level(lst: list[CountyDemographics]):
    per_total = population_total(lst)
    pov_total = population_below_poverty_level(lst)
    try:
        ed_percent = pov_total / per_total
    except ZeroDivisionError:
        ed_percent = 0.0
    return ed_percent * 100

#Part 5

def education_greater_than(lst: list[CountyDemographics], ed_key: str, numb: float):
    filter_lst = []
    for county in lst:
        compare_percent = county.education.get(ed_key)
        if compare_percent > numb:
            filter_lst.append(county)
    return filter_lst


def education_less_than(lst: list[CountyDemographics], ed_key: str, numb: float) -> list[CountyDemographics]:
    return [county for county in lst if county.education.get(ed_key) < numb]

def ethnicity_greater_than(lst: list[CountyDemographics], eth_key: str, numb: float) -> list[CountyDemographics]:
    return [county for county in lst if county.ethnicities.get(eth_key) > numb]

def ethnicity_less_than(lst: list[CountyDemographics], eth_key: str, numb: float) -> list[CountyDemographics]:
    return [county for county in lst if county.ethnicities.get(eth_key) < numb]

def below_poverty_level_greater_than(lst: list[CountyDemographics], numb: float) -> list[CountyDemographics]:
    return [county for county in lst if county.income.get("Persons Below Poverty Level") > numb]

def below_poverty_level_less_than(lst: list[CountyDemographics], numb: float) -> list[CountyDemographics]:
    return [county for county in lst if county.income.get("Persons Below Poverty Level") < numb]
