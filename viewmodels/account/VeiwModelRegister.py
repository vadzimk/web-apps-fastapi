from starlette.requests import Request

from viewmodels.base.ViewModelBase import ViewModelBase


class ViewModelRegister(ViewModelBase):
    def __init__(self, request: Request):
        super(ViewModelRegister, self).__init__(request)