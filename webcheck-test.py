# WebCheck tester
# https://github.com/arzynik/sd-webcheck

# read the config and pass it to the parser so we can test without reloading our server over and over

from WebCheck import WebCheck
from ConfigParser import ConfigParser

config = ConfigParser()
config.read('/etc/sd-agent/config.cfg')

check = WebCheck('','',config._sections).run()
print check