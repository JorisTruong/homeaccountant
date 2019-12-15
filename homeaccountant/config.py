import os
import yaml
import pathlib


class SERVER:
    HOSTNAME = '127.0.0.1'
    PORT = 8080

    class REGISTRATION:
        ALLOW = True
        REGEX = r'.*'
        EMAIL_CONFIRMATION = False

    class SENDMAIL:
        ENABLED = False
        USE_SSL = True
        HOSTNAME = None
        PORT = None
        USERNAME = None
        PASSWORD = None


class DATABASE:
    class POSTGRES:
        HOSTNAME = '127.0.0.1'
        PORT = 5432
        USERNAME = None
        PASSWORD = None
        DATABASE = None


def update_attributes(d, prefix=None):
    for k, v in d.items():
        k = k.upper()
        try:
            if isinstance(v, dict):
                if prefix == None:
                    update_attributes(v, prefix=k)
                else:
                    update_attributes(v, prefix='.'.join([prefix, k]))
            else:
                if prefix == None:
                    obj = globals()[k]
                else:
                    prefixes = prefix.split('.')
                    obj = globals()[prefixes[0]]
                    for i in prefixes[1:]:
                        obj = getattr(obj, i)
                setattr(obj, k, v)
        except Exception as e:
            pass


def load_configuration(path):
    with open(path, 'r') as f:
        d = yaml.load(f, Loader=yaml.FullLoader)
    update_attributes(d)

try:
    load_configuration(os.path.join(str(pathlib.Path.home()),
                                    '.config/homeaccountant/config.yaml'))
except:
    print("File not found.")
