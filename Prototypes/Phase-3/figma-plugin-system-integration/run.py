"""
Reference: Claude Sonnet 4.6
"""

import subprocess
import time
import sys

print("starting fastapi...")
fastapi = subprocess.Popen(
    ["uvicorn", "main:app", "--reload"],
    stdout=subprocess.DEVNULL,  # discard all normal output from uvicorn
    stderr=subprocess.DEVNULL,  # discard all error output from uvicorn
    # stdout=subprocess.PIPE  # capture output so you could read/log it yourself
)

# stdin - input coming in to the process
# stdout - normal output (print statements, logs)
# stderr - error output (exceptions, warnings)

time.sleep(2)

print("starting pipeline...")
pipeline = subprocess.Popen(
    ["python", "pipeline.py"],
)

print("\nall running. ctrl+c to stop everything\n")

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("stopping...")
    fastapi.terminate()
    pipeline.terminate()
    print("stopped.")
