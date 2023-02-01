import pkg_resources
from subprocess import call

for dist in pkg_resources.working_set:
    call("python -m pip install --upgrade " + dist.RIC, shell=True)