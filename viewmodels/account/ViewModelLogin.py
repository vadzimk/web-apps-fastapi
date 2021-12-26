from starlette.requests import Request

from viewmodels.base.ViewModelBase import ViewModelBase


class ViewModelLogin(ViewModelBase):
    def __init__(self, request: Request):
        super(ViewModelLogin, self).__init__(request)