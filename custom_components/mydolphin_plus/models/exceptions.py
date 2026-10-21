class LoginError(Exception):
    def __init__(self, message: str = "Failed to login"):
        super().__init__(message)
        self.error = message


class TransientLoginError(LoginError):
    """Login could not be checked (network down, timeout, server error, rate limit).

    The stored tokens may still be valid, so callers should retry later rather
    than discard them and ask the user to sign in again.
    """
