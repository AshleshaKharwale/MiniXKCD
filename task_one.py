"""
CLI tool to fetch data from "https://xkcd.com/"

python task_one.py --max 87  --any 15
"""

import argparse
import requests
from random import randrange
from typing import List
from pprint import pprint


home_url = "https://xkcd.com/"
relative_url = "{0}/info.0.json"


def rand_gen(start: int = 1, stop: int = 87, limit: int = 15) -> List[int]:
    """

    Args:
        start (int): first numeric value of the range
        stop (int): last numeric value of the range
        limit (int): number of results to yield

    Returns:
        List[int]: random values in range(start:stop) with count limited
        to `limit`
    """

    result = [randrange(start, stop+1) for i in range(limit)]
    return result


def sample2():
    """
    Creating sample function to test merge conflict
    :return: None
    """
    print("Sample 2")


def sample():
    """
    Creating sample function to test merge conflict
    :return: None
    """
    print("Sample merge conflict")


def get_details(num_list):
    absolute_url = home_url+relative_url
    for num in num_list:
        response = requests.get(absolute_url.format(num))
        pprint(response.json())
        print("-----------"*10)


if __name__ == "__main__":
    example = """example:
    
    python task_one.py --max 87  --any 15
    """

    parser = argparse.ArgumentParser(
        description="CLI tool to fetch resource(s) from API",
        epilog=example
    )

    parser.add_argument(
        "-m",
        "--max",
        type=int,
        default=87,
        help="max number of resources to be fetched"
    )

    parser.add_argument(
        "-a",
        "--any",
        type=int,
        default=15,
        help="random sized chunk of resources to be fetched"
    )

    args = parser.parse_args()
    comic_number_set = rand_gen(1, args.max, args.any)
    # breakpoint()
    get_details(comic_number_set)



