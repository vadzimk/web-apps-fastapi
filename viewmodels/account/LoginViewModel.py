from starlette.requests import Request

from viewmodels.base.BaseViewModel import BaseViewModel


class LoginViewModel(BaseViewModel):
    def __init__(self, request: Request):
        super(LoginViewModel, self).__init__(request)