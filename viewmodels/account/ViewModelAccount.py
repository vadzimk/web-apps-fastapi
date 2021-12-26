from starlette.requests import Request

from viewmodels.base.ViewModelBase import ViewModelBase


class ViewModelAccount(ViewModelBase):
    def __init__(self, request: Request):
        super(ViewModelAccount, self).__init__(request)