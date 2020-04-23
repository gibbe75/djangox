import os

try:
    environment = os.environ['ENV_CHOICE']
except KeyError:
    environment = "1"

# 1: local / 2: prod
if environment == "1":
    from .settings_local import *
elif environment == "2":
    from .settings_prod import *