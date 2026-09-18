# log_util.py
# Simple timestamped logger for KM-Waechter.
# Written in 2013. Modernised 2025: with-block for file handle, dead debug branch removed.

import time

LOG_LINES: list[str] = []  # module-level buffer; cleared after each flush


def log(message: str) -> None:
    """Append a timestamped line to the buffer and print it."""
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}"
    LOG_LINES.append(line)
    print(line)


def flush_log(path: str) -> None:
    """Write all buffered lines to path (append mode) and clear the buffer."""
    with open(path, "a") as f:
        for line in LOG_LINES:
            f.write(line + "\n")
    LOG_LINES.clear()
