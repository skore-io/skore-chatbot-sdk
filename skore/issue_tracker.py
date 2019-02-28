import sentry_sdk
from sentry_sdk import capture_exception
from functools import wraps

ACTION_FAILURE = 'failure'

def catchable(original_function):
    @wraps(original_function)
    def wrapped(*args, **kwargs):
        try:
            return original_function(*args, **kwargs)
        except Exception as exception:
          this = args[0]
          sentry_dns = this.db.bot.settings['sentry_dns']
          environment = this.db.bot.settings['environment']
          sentry_sdk.init(sentry_dns, environment=environment)
          sentry_sdk.capture_exception(exception)

        return this.respond(message=None, action=ACTION_FAILURE)

    return wrapped