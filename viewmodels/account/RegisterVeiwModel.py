from typing import Optional

from starlette.requests import Request

from viewmodels.base.BaseViewModel import BaseViewModel


class RegisterViewModel(BaseViewModel):
    def __init__(self, request: Request):
        super(RegisterViewModel, self).__init__(request)
        self.email: Optional[str] = None
        self.password: Optional[str] = None
        self.name: Optional[str] = None

    async def load(self):
        # grab data from request.form
        form = await self.request.form()
        # assign fields first in case error their values are returned back
        self.name = form.get('name')
        self.password = form.get('password')
        self.email = form.get('email')

        # validate fields
        if not self.name or not self.name.strip():
            self.error = "Your name is required"
        elif not self.email or not self.email.strip():
            self.error = "Your email is required"
        elif not self.password or len(self.password)<5:
            self.error = "Your password is required and must be at least 5 characters"

