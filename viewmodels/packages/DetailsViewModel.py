

from starlette.requests import Request


from services import package_service
from viewmodels.base.BaseViewModel import BaseViewModel


class DetailsViewModel(BaseViewModel):
    def __init__(self, package_name: str, request: Request):
        super(DetailsViewModel, self).__init__(request)
        self.package_name = package_name
        self.package = package_service.get_package_by_name(package_name)
        self.latest_release = package_service.get_latest_release_for_package(package_name)
        self.latest_version = "0.0.0"
        self.is_latest = True
        self.maintainers = []

        if not self.package or not self.latest_release:
            # return 404
            return

        self.latest_version = self.latest_release.version
        self.maintainers = self.package.maintainers
