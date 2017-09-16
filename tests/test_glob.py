"""Tests for aiofiles glob module."""

from os.path import join, dirname
import glob as system_glob
import aiofiles.glob
import pytest


@pytest.mark.asyncio
def test_glob():
    """Test the glob call."""
    directory = join(dirname(__file__), 'resources')
    pathname = '{}/**'.format(directory)
    system_glob_result = system_glob.glob(pathname)

    glob_result = yield from aiofiles.glob.glob(pathname)

    assert glob_result == system_glob_result
