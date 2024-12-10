import multiprocessing
import os

# Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Host and port - Always bind to 0.0.0.0 to listen on all interfaces
bind = f"0.0.0.0:{os.getenv('PORT', '8000')}"

# Worker timeout
timeout = 120

# Access log format
accesslog = '-'  # Log to stdout
errorlog = '-'   # Log to stdout

# Worker class
worker_class = 'gevent'  # Use gevent for async support
