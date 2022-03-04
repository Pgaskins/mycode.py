#!/usr/bin/env python3
def get_all_keys(farms):


    
    for key,value in farms[key].items():
        yield key
        if isinstance(value, dict):
            yield from get_all_keys(value)
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]        
for x in get_all_keys(farms):
    print(x)

get_all_keys()

    

 
