# Copyright 2019, Digi International Inc.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from typing import Any, Iterator, List, Optional, Tuple

sep: str = ...


def chdir(path: str) -> None:
    """
    Changes current directory.

    :param path: Path to change to.
    """
    ...

def getcwd() -> str:
    """
    Gets the current directory.

    :return: Current directory.
    """
    ...

def ilistdir(path: str=".") -> Iterator[Tuple]:
    """
    Returns an iterator which then yields tuples corresponding to the entries
    in the directory that it is listing. With no argument it lists the current
    directory, otherwise it lists the directory given by ``path``.

    The tuples have the form ``(name, type, inode[, size])``:

    * ``name`` is a string (or bytes if dir is a bytes object) and is the name
      of the entry.
    * ``type`` is an integer that specifies the type of the entry, with 0x4000
      for directories and 0x8000 for regular files.
    * ``inode`` is an integer corresponding to the inode of the file, and may
      be 0 for filesystems that don't have such a notion.
    * Some platforms may return a 4-tuple that includes the entry's size. For
      file entries, ``size`` is an integer representing the size of the file or
      -1 if unknown. Its meaning is currently undefined for directory entries.

    :param path: Path to list its elements.

    :return: An iterator with a tuple for each entry in the path.
    """
    ...

def listdir(path: str=".") -> List:
    """
    Lists the specified path or the current one if ``path`` is not provided.

    :param path: The path to list. If this parameter is not provided, the
        method lists the current path.

    :return: List containing the name of the elements in the path.
    """
    ...

def mkdir(path: str) -> None:
    """
    Creates a new directory.

    :param path: Name of the directory to create.
    """
    ...

def remove(path: str) -> None:
    """
    Removes a file.

    :param path: Path of the file to remove.
    """
    ...

def rename(old_path: str, new_path: str) -> None:
    """
    Renames a file or directory.

    :param old_path: Name of the file to rename.
    :param new_path: New name of the file.
    """
    ...

def replace(old_path: str, new_path: str) -> None:
    """
    Replaces a file or directory (``new_path``) with another (``old_path``).

    :param old_path: Path of the file or directory to be replaced.
    :param new_path: Path of the file or directory that replaces ``old_path``.
    """
    ...

def rmdir(dir: str) -> None:
    """
    Removes a directory. Fails if ``dir`` is not empty.

    :param dir: Path of the directory to remove.
    """
    ...

def statvfs(path: str) -> Tuple:
    """
    Gets the status of a fileystem.

    Returns a tuple with the filesystem information in the following order:

    * ``f_bsize`` – file system block size
    * ``f_frsize`` – fragment size
    * ``f_blocks`` – size of fs in f_frsize units
    * ``f_bfree`` – number of free blocks
    * ``f_bavail`` – number of free blocks for unpriviliged users
    * ``f_files`` – number of inodes
    * ``f_ffree`` – number of free inodes
    * ``f_favail`` – number of free inodes for unpriviliged users
    * ``f_flag`` – mount flags
    * ``f_namemax`` – maximum filename length

    :param path: Path of the filesystem to get its status.

    :return: Tuple with the status of a filesystem.
    """
    ...

def unlink(path: str) -> None:
    """
    Removes (deletes) a file. This function is semantically identical to
    ``uos.remove()``.

    :param path: Path of the file to remove.
    """
    ...

def sync() -> None:
    """
    Synchronizes all filesystems.
    """
    ...

def urandom(n: int) -> bytes:
    """
    Returns a bytes object with ``n`` random bytes generated by the hardware
    random number generator.

    :param n: Number of random bytes to generate.

    :return: Bytes object with the generated random bytes.
    """
    ...

def compile(source_file: str, mpy_file: Optional[str]=None) -> None:
    """
    Compiles Python source code in ``source_file`` and stores in a file with
    an .mpy extension.

    :param source_file: Python source filename to compile.
    :param mpy_file: Destination mpy compiled file.
    """
    ...

def bundle(*args: Optional[str]) -> Optional[List]:
    """
    Embeds modules into the flash of the device where they can run in-place,
    with minimal heap usage.

    If the method is called without parameters it displays a list of modules
    embedded in the flash. Calling the method with parameter ``None`` erases
    the modules embedded in the flash.

    :param args: Empty to list the embedded modules, ``None`` to erase the
        embedded modules or the name of the modules to embed in flash.

    :return: ``None`` if the method is called with parameters or a list with
        the name of the embedded modules when the parameter is ``None``.
    """
    ...

def format() -> None:
    """
    Re-formats the filesystem and creates the default directory structure.
    """
    ...

def hash(secure_file: Optional[str]) -> Any:
    """
    Returns a 32-byte bytes object with the sha256 hash digest of a secure
    file. You can use this value to verify that a secure file matches an
    unencrypted copy of the file.

    If secure_file is not specified, it returns a string identifying the hash
    method ('sha256').

    :param secure_file: Secure file to get its hash.

    :return: 32-byte bytes object with the sha256 hash digest of a secure
        file or the hash identifier if ``secure_file`` is not provided.
    """
    ...