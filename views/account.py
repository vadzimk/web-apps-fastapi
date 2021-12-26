from fastapi_chameleon import template
from fastapi import APIRouter
from starlette.requests import Request

from viewmodels.account.VeiwModelRegister import ViewModelRegister
from viewmodels.account.ViewModelAccount import ViewModelAccount
from viewmodels.account.ViewModelLogin import ViewModelLogin

router = APIRouter()


@router.get('/account')
def account(request: Request):
    vm = ViewModelAccount(request)
    return vm.to_dict()


@router.get('/account/register')
def register(request: Request):
    vm = ViewModelRegister(request)
    return vm.to_dict()


@router.get('/account/login')
def login(request: Request):
    vm = ViewModelLogin(request)
    return vm.to_dict()


@router.get('/account/logout')
def logout(request: Request):
    return {}
