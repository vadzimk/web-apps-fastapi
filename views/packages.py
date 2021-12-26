from typing import Dict

from fastapi import APIRouter
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.home.IndexViewModel import IndexViewModel
from viewmodels.packages.DetailsViewModel import DetailsViewModel

router = APIRouter()


@router.get('/project/{package_name}')
@template(template_file='packages/details.html')
def details(package_name: str, request: Request) -> Dict:
    vm = DetailsViewModel(package_name, request)
    return vm.to_dict()