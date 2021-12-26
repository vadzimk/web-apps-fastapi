# sqlalchemy queries will be here
import datetime
from typing import List, Optional

from model.Package import Package
from model.Release import Release


def release_count() -> int:
    return 3


def package_count():
    return 4


def latest_packages(limit: int = 5) -> List:
    return [
               {'id': 'fastapi', 'summary': "A great web framework"},
               {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
               {'id': 'httpx', 'summary': "Requests for an async world"},
           ][:limit]


def get_package_by_name(package_name: str)->Optional[Package]:
    package = Package(package_name,
                      "this is the summary",
                      "full details here",
                      "https://fastapi.tiangolo.com",
                      "MIT", "Sebastian Ramirez")
    return package


def get_latest_release_for_package(package_name:str)->Optional[Release]:
    return Release("1.2.0", datetime.datetime.now())