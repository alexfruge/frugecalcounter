from pathlib import Path
import json
from time import time

def write_finished_item(curr_food_dict):
    fdc_id = curr_food_dict["fdc_id"]
    savepath = Path(f"data/foods/{fdc_id}.json")

    with open(savepath, "w") as out:
        json.dump(curr_food_dict, out)


def parse_foodnutrient():
    """Parses data found within food_nutrient.csv, which contains the amount of a given nutrient per 100g of a food item"""
    food_nutrient_path = Path("fooddata/food_nutrient.csv")

    print("starting parse & save")
    start = time()
    with open(food_nutrient_path, "r") as fn_file:
        lines = fn_file.readlines()

        current_fdc_id = None
        for line in lines[1:]:
            elems = line.replace("\"", "").replace("\n", "").split(",")

            if current_fdc_id != elems[1]:
                if current_fdc_id == None: # first pass
                    curr_food_dict = {"fdc_id": elems[1], "nutrients": dict()}

                write_finished_item(curr_food_dict)
                current_fdc_id = elems[1]
                curr_food_dict = {"fdc_id": elems[1], "nutrients": dict()}
            
            if elems[3] != "0.0": # data is strings...
                curr_food_dict["nutrients"][elems[2]] = float(elems[3])

    print(f"Finished in {time() - start}")

def parse_foodportion():
    """Parses food_portion.csv, which gives a food's weight per serving in grams"""


def parse_food():
    """Parses food.csv, which gives a food's name based on its fdc_id"""


parse_foodnutrient()