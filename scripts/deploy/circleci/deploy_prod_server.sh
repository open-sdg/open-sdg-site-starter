#!/usr/bin/env bash
# This script deploys the built site to the server.

SERVER="37.252.79.51"
USERNAME="rubo"
FOLDER="/var/www/html/"

# The fully built site is already available at ~/repo/_site.
scp -r ~/repo/_site/* $USERNAME@$SERVER:$FOLDER
