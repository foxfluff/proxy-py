# proxy-py
Simple 1:1 proxy designed to be easily deployable in environments with limited capabilities.

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