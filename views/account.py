import fastapi.responses
from fastapi_chameleon import template
from fastapi import APIRouter
from starlette import status
from starlette.requests import Request

from services import user_service
from utils import cookie_auth
from viewmodels.account.RegisterVeiwModel import RegisterViewModel
from viewmodels.account.AccountViewModel import AccountViewModel
from viewmodels.account.LoginViewModel import LoginViewModel

router = APIRouter()


@router.get('/account')
@template(template_file='account/index.html')
def account(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get('/account/register')
@template(template_file='account/register.html')
def register(request: Request):
    print("register GET")
    vm = RegisterViewModel(request)
    return vm.to_dict()

@router.post('/account/register')
@template(template_file='account/register.html')
async def register(request: Request):
    print("register POST")
    vm = RegisterViewModel(request)
    await vm.load()   # accept the data from the post request
    if vm.error:
        # returns the same data back to correct it
        return vm.to_dict()

    # Create account
    account = user_service.create_account(vm.name, vm.email, vm.password)
    # login user:
    # by default fastapi redirects to post, need to change it with status_code parameter
    response = fastapi.responses.RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, account.id)
    return response

@router.get('/account/login')
@template(template_file='account/login.html')
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.post('/account/login')
@template(template_file='account/login.html')
async def login(request: Request):
    vm = LoginViewModel(request)
    await vm.load_form()
    if vm.error:
        return vm.to_dict()
    user = user_service.login_user(vm.email, vm.password)
    if not user:
        vm.error = 'The email or password are incorrect'
        return vm.to_dict()
    response = fastapi.responses.RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, user.id)
    return response

@router.get('/account/logout')
def logout(request: Request):
    response = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)
    return response
