from fastapi_chameleon import template
from fastapi import APIRouter
from starlette.requests import Request

from viewmodels.account.RegisterVeiwModel import RegisterViewModel
from viewmodels.account.AccountViewModel import AccountViewModel
from viewmodels.account.LoginViewModel import LoginViewModel

router = APIRouter()


@router.get('/account')
def account(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get('/account/register')
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.get('/account/login')
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.get('/account/logout')
def logout(request: Request):
    return {}
