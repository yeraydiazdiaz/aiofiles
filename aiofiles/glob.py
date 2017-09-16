"""Async executor version of the `glob` function."""
import glob
import aiofiles.os

wrap = aiofiles.os.wrap

glob = wrap(glob.glob)
