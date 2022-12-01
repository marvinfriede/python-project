"""
Entry point for command line interface.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from .__version__ import __version__
from .maths import square_a_number as square

__all__ = ["__version__", "maths", "square"]


def main(argv: Sequence[str] | None = None) -> int:
    # get command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=float, help="Number to square.")
    args = parser.parse_args(argv)

    # print result
    print(square(args.number))

    return 0


if __name__ == "__main__":
    sys.exit(main())
