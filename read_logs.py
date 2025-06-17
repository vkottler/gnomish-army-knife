#!/usr/bin/env python

# built-in
from os import SEEK_END
from pathlib import Path
import sys
from time import sleep

# third-party
from vcorelib.math import default_time_ns, nano_str


def main(argv: list[str]) -> int:
    """Attempt to read from a file."""

    with Path(argv[0]).open() as log:
        log.seek(0, SEEK_END)

        prev_update = default_time_ns()

        while True:
            data = log.read()
            if data:
                curr_update = default_time_ns()
                interval = curr_update - prev_update
                prev_update = curr_update
                print(
                    (
                        f"interval: {nano_str(interval, is_time=True)}s, "
                        f"{len(data.splitlines())} lines"
                    )
                )

            sleep(0.1)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
