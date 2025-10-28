#!/bin/bash

# This script exists because when the container is not running with -t, there will be no logs.
# By disabling the Python buffer, we circumvent this.

mitmproxy="/usr/local/bin/mitmdump"
entrypoint="main.py"

cd -- "$(dirname -- "${BASH_SOURCE[0]}")"

exec $(head -n 1 "$mitmproxy" | sed "s/#!//g" | cut -f1 -d" ") -u "$mitmproxy" -s "$entrypoint"
