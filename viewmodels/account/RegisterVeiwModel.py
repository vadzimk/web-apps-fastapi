from starlette.requests import Request

from viewmodels.base.BaseViewModel import BaseViewModel


class RegisterViewModel(BaseViewModel):
    def __init__(self, request: Request):
        super(RegisterViewModel, self).__init__(request)