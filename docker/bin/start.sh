#!/bin/bash
chmod +x /root/pushflag.sh
touch /app/temp.sh
chmod +x /app/temp.sh
/root/pushflag.sh
flask run -h 0.0.0.0 -p 5000