import requests
from bs4 import BeautifulSoup as bs

def generate_oily():
    return {
        "salicylic acid": True,
        "benzoyl peroxide": True,
        "niacinamide": True,
        "glycolic acid": True,
        "hyaluronic acid": True,
        "dimethicone": True,
        "sodium hyaluronate": True,
        "retinol": True,
        "l-ascorbic acid": True,
        "vitamin c": True,
        "clay": True,

        "sd alcohol": False,
        "denatured alcohol": False,
        "tocopheryl acetate": False,
        "witch hazel": False,
        "sodium c14-16 olefin sulfate": False,
        "sodium lauryl sulfate": False,
        "fragrance": False
    }

def generate_dry():
    return {
        "polysorbate 85": True,
        "butylene glycol": True,
        "cocamidopropyl betaine": True,
        "urea": True,
        "cetearyl alcohol": True,
        "shea butter": True,
        "sodium hyaluronate": True,
        "stearic acid": True,
        "propylene glycol": True,
        "glycerin": True,

        "sd alcohol": False,
        "denatured alcohol": False,
        "isopropyl alcohol": False,
        "witch hazel": False,
        "sodium laureth sulfate": False,
        "menthol": False,
        "sodium lauryl sulfate": False,
        "fragrance": False
    }

def generate_normal():
    return {
        "glycolic acid": True,
        "panthenol": True,
        "sodium hyaluronate": True,
        "retinol": True,
        "dimethicone": True,
        "hyaluronic acid": True,

        "sd alcohol": False,
        "denatured alcohol": False,
        "isopropyl alcohol": False,
        "witch hazel": False,
        "sodium laureth sulfate": False,
        "menthol": False,
        "sodium lauryl sulfate": False,
        "fragrance": False,
        "sodium chloride": False
    }

def main():
    # True if good, False if bad
    # all strings are lower case and anything read in will be converted to lower case as well

    oily, dry, normal = generate_oily(), generate_dry(), generate_normal()

    

if __name__ == "__main__":
    main()