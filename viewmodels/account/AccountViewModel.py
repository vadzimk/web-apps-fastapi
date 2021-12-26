from starlette.requests import Request

from viewmodels.base.BaseViewModel import BaseViewModel


class AccountViewModel(BaseViewModel):
    def __init__(self, request: Request):
        super(AccountViewModel, self).__init__(request)