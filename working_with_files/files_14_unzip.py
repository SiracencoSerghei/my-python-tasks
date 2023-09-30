"""Utility functions for copying and archiving files and directory trees.

XXX The functions here don't copy the resource fork or other metadata on Mac."""
import shutil


def unpack(archive_path, path_to_unpack):
    """Unpack archive to specified path."""
    try:
        shutil.unpack_archive(archive_path, path_to_unpack)
    except ValueError:
        print('Not registered extension')
