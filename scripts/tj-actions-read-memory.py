#!/usr/bin/env python3
import os
import sys
  
def get_pid():
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
    for pid in pids:
        try:
            with open(os.path.join('/proc', pid, 'cmdline'), 'rb') as cmdline_f:
                if b'Runner.Worker' in cmdline_f.read():
                    return pid
        except (IOError, PermissionError):
            continue
    raise Exception('Cannot find Runner.Worker PID')

if __name__ == "__main__":
    try:
        pid = get_pid()
        print(f"Found Runner.Worker process with PID: {pid}")
        mem_path = f"/proc/{pid}/mem"

        try:
            with open(mem_path, 'rb', 0) as mem_f:
                print("Successfully opened memory file")
                # Example: read the first 4096 bytes of memory
                # You must know the address to seek if you skip /maps
                mem_f.seek(0)
                chunk = mem_f.read(4096)
                sys.stdout.buffer.write(chunk)

        except PermissionError as e:
            print("Error: Permission denied. This script needs to be run with root privileges.")
            print(f"Details: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error accessing process memory: {e}")
            sys.exit(1)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
