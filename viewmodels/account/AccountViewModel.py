from starlette.requests import Request

from model.User import User
from viewmodels.base.BaseViewModel import BaseViewModel


class AccountViewModel(BaseViewModel):
    def __init__(self, request: Request):
        super(AccountViewModel, self).__init__(request)
        self.user = User('Michael', 'michael@gmail.com', 'afbaret')