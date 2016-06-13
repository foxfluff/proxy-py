# proxy-py
Simple 1:1 proxy designed to be easily deployable in environments with limited capabilities.

WARNING: This program is super gross and there is good reason for that (mainly why it is in a single py document instead of an egg or multiple py files).

The primary reasoning for this to be in a single py document is to make it easier for deployment in an environment with extremely limited capabilities.  For example: if you only have a console that allows you to run a handful of commands (like echo and python), and have read/write access to a location on that system, then you should be able to fairly easily deploy this by just copying the code directly in to the terminal and executing.  (Note: it might be beneficial to base64 encode this if possible in your situation.)

This program is not meant to be a enterprise level or super efficient proxy, it is meant to be a hack job that is easy(ish) to setup when you desperately need it.

## Usage:

```
usage: proxy.py [-h] [-l LOCAL_ADDRESS] -p LOCAL_PORT -r REMOTE_ADDRESS -d
                REMOTE_PORT

Simple 1:1 proxy - Example usage: proxy.py -p 8080 -r 192.168.0.1 -d 80

optional arguments:
  -h, --help            show this help message and exit
  -l LOCAL_ADDRESS, --local-addr LOCAL_ADDRESS
                        The local address to bind to (default: 0.0.0.0)
  -p LOCAL_PORT, --local-port LOCAL_PORT
                        The local TCP port to bind to
  -r REMOTE_ADDRESS, --remote-addr REMOTE_ADDRESS
                        The remote address to connect to
  -d REMOTE_PORT, --remote-port REMOTE_PORT
                        The remote port to connect to
```