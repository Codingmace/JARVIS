
import platform
import sys
#print(platform.system())
#print(platform.platform())



def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"

print("""Python version: %s
linux_distribution: %s
system: %s
machine: %s
platform: %s
uname: %s
version: %s
mac_ver: %s
""" % (
sys.version.split('\n'),
linux_distribution(),
platform.system(),
platform.machine(),
platform.platform(),
platform.uname(),
platform.version(),
platform.mac_ver(),
))

print(platform.uname()[0])