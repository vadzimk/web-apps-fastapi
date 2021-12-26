from fastapi import APIRouter
from fastapi_chameleon import template
from starlette.requests import Request
from typing import Dict

from viewmodels.base.BaseViewModel import BaseViewModel
from viewmodels.home.IndexViewModel import IndexViewModel

router = APIRouter()


# {
#         'package_count': 1,
#         'release_count': 1,
#         'user_count': 1,
#         'packages': []
#     }
@router.get('/')
@template(template_file='home/index.html')
def index(request: Request) -> Dict:
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get('/about')
@template(template_file='home/about.html')
def about(request: Request):
    vm = BaseViewModel(request)
    # todo: use vm
    return vm.to_dict()
