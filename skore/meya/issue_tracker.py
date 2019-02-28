from functools import wraps
import sys
import traceback
import time, datetime
from skore.integration_services import IntegrationServices

ACTION_FAILURE = 'failure'

def catchable(original_function):
    @wraps(original_function)
    def wrapped(*args, **kwargs):
        try:
            return original_function(*args, **kwargs)
        except Exception as exception:
            this = args[0]
            this.log('enter catchable', type='misc', status='info')

            # exc_type, exc_obj, exc_tb = sys.exc_info()
            # line = traceback.extract_tb(exc_tb)[-1][1]
            # error_object = _error_object(this, exception, line)

            # service = IntegrationServices(
            #     this.db.bot.settings['skore_host'],
            #     this.db.bot.settings['environment']
            # )
            # status_code = service.send_meya_error(error_object, _header(this))
            # this.log(status_code, type='misc', status='info')        
        return this.respond(message=None, action=ACTION_FAILURE)

    return wrapped

def _header(meya):
    environment = meya.db.bot.settings['environment']
    secret_key = meya.db.bot.settings['integrations_secret_key']
    bot_name = meya.db.bot.settings['bot_name']

    return {
        'Content-Type': 'application/json',
        'App-Name': bot_name,
        'Environment': environment,
        'Integrations-Secret-Key': secret_key
    }

def _error_object(meya, exception, line):
    user = meya.db.user
    environment = meya.db.bot.settings['environment']

    return {
        'environment': environment,
        'message': exception.__doc__,
        'exception': {
            'name': exception.__class__.__name__,
            'message': exception.message,
            'component_name': meya.__class__.__name__,
            'line': line,
            'occurred_at': _datetime_now()
        },
        'user': {
            'meya_user_id': user.id,
            'skore_user_id': user.get('skore_user_id'),
            'skore_company_id': user.get('skore_company_id'),
            'email': user.get('email'),
            'name': user.get('name')
        }
    }

def _datetime_now():
    timestamp = time.time()
    time_format = '%Y-%m-%d %H:%M:%S'

    return datetime.datetime.fromtimestamp(timestamp).strftime(time_format)
