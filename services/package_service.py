# sqlalchemy queries will be here
from typing import List


def release_count()->int:
    return 3


def package_count():
    return 4


def latest_packages(limit: int=5)->List:
    return []