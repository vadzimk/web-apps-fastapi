from services import package_service, user_service
from viewmodels.base.BaseViewModel import BaseViewModel
from starlette.requests import Request
from typing import List


class IndexViewModel(BaseViewModel):
    def __init__(self, request: Request):
        super().__init__(request)
        self.release_count: int = package_service.release_count()
        self.package_count: int = package_service.package_count()
        self.user_count: int = user_service.user_count()
        self.packages: List = package_service.latest_packages(limit=5)
