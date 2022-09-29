"""Gunicorn configuration file."""

timeout = 60
bind = "0.0.0.0:8000"
forwarded_allow_ips = "*"
workers = 2
