import multiprocessing
import os

# Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Host and port
bind = f"{os.getenv('HOST', '0.0.0.0')}:{os.getenv('PORT', '8000')}"

# Worker timeout
timeout = 120

# Access log format
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
capture_output = True  # This will also send logs to stdout

# Worker class
worker_class = 'gevent'  # Use gevent for async support
