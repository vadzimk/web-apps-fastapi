from starlette.requests import Request

from viewmodels.base.BaseViewModel import BaseViewModel


class LoginViewModel(BaseViewModel):
    def __init__(self, request: Request):
        super(LoginViewModel, self).__init__(request)
        self.email = ''
        self.password = ''

    async def load_form(self):
        form = await self.request.form()
        self.email = form.get('email', '').lower().strip()
        self.password = form.get('password', '').strip()

        if not self.email:
            self.error = 'You must specify email'
        elif not self.password:
            self.error = 'You must specify password'
