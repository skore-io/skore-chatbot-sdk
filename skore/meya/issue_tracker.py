from functools import wraps
import sys
import traceback
import time, datetime
import requests

ACTION_FAILURE = 'failure'
MEYA_ERROR = "{host}/integration/v1/meya/errors"

def catchable(original_function):
    @wraps(original_function)
    def wrapped(*args, **kwargs):
        try:
            return original_function(*args, **kwargs)
        except Exception as exception:
            this = args[0]

            exc_type, exc_obj, exc_tb = sys.exc_info()
            line = traceback.extract_tb(exc_tb)[-1][1]
            error_object = _error_object(this, exception, line)
            host = this.db.bot.settings['skore_host']
            try:
                status_code = _send_meya_error(host, _header(this), error_object)
            except Exception as exception:
                this.log(exception.message, type='misc', status='info')

            this.log('send_meya_error - status_code:%s' % status_code, type='misc', status='info')

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


def _send_meya_error(host, headers, data):
    url = MEYA_ERROR.format(host=host)
    response = requests.post(url, json=data, headers=headers)
    return response.status_code
