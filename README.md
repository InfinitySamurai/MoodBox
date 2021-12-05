# MoodBox

This is a simple little project that runs a rapsberry pi "MoodBox". It is a box with 4 buttons, 4 LEDs, and a switch. It's used as a quick and easy means to record a datapoint for how you're feeling at any time by simply pushing a button.

Service is run using system from /etc/systemd/system/mood-box.service
Server for serving csv is from /etc/systemd/system/mood-box-server.service 

systemctl start <service>
systemctl enable <service>

Steps for setting up service followed from https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267
