from authlib.common.errors import AuthlibBaseError


OAuthError = AuthlibBaseError


class MissingRequestTokenError(OAuthError):
    error = 'missing_request_token'


class MissingTokenError(OAuthError):
    error = 'missing_token'


class TokenExpiredError(OAuthError):
    error = 'token_expired'


class UnsupportedTokenTypeError(OAuthError):
    error = 'unsupported_token_type'


class MismatchingStateError(OAuthError):
    error = 'mismatching_state'
    description = 'CSRF Warning! State not equal in request and response.'
