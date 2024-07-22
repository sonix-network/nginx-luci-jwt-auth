r"""Wrapper for jwt.h

Generated with:
/home/bluecmd/.local/bin/ctypesgen -ljwt include/jwt.h

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["jwt"] = load_library("jwt")

# 1 libraries
# End libraries

# No modules

__off_t = c_long# /usr/include/bits/types.h: 152

__off64_t = c_long# /usr/include/bits/types.h: 153

__time_t = c_long# /usr/include/bits/types.h: 160

# /usr/include/bits/types/struct_FILE.h: 49
class struct__IO_FILE(Structure):
    pass

FILE = struct__IO_FILE# /usr/include/bits/types/FILE.h: 7

# /usr/include/bits/types/struct_FILE.h: 36
class struct__IO_marker(Structure):
    pass

# /usr/include/bits/types/struct_FILE.h: 37
class struct__IO_codecvt(Structure):
    pass

# /usr/include/bits/types/struct_FILE.h: 38
class struct__IO_wide_data(Structure):
    pass

_IO_lock_t = None# /usr/include/bits/types/struct_FILE.h: 43

struct__IO_FILE.__slots__ = [
    '_flags',
    '_IO_read_ptr',
    '_IO_read_end',
    '_IO_read_base',
    '_IO_write_base',
    '_IO_write_ptr',
    '_IO_write_end',
    '_IO_buf_base',
    '_IO_buf_end',
    '_IO_save_base',
    '_IO_backup_base',
    '_IO_save_end',
    '_markers',
    '_chain',
    '_fileno',
    '_flags2',
    '_old_offset',
    '_cur_column',
    '_vtable_offset',
    '_shortbuf',
    '_lock',
    '_offset',
    '_codecvt',
    '_wide_data',
    '_freeres_list',
    '_freeres_buf',
    '__pad5',
    '_mode',
    '_unused2',
]
struct__IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', String),
    ('_IO_read_end', String),
    ('_IO_read_base', String),
    ('_IO_write_base', String),
    ('_IO_write_ptr', String),
    ('_IO_write_end', String),
    ('_IO_buf_base', String),
    ('_IO_buf_end', String),
    ('_IO_save_base', String),
    ('_IO_backup_base', String),
    ('_IO_save_end', String),
    ('_markers', POINTER(struct__IO_marker)),
    ('_chain', POINTER(struct__IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_char),
    ('_shortbuf', c_char * int(1)),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('_codecvt', POINTER(struct__IO_codecvt)),
    ('_wide_data', POINTER(struct__IO_wide_data)),
    ('_freeres_list', POINTER(struct__IO_FILE)),
    ('_freeres_buf', POINTER(None)),
    ('__pad5', c_size_t),
    ('_mode', c_int),
    ('_unused2', c_char * int((((15 * sizeof(c_int)) - (4 * sizeof(POINTER(None)))) - sizeof(c_size_t)))),
]

time_t = __time_t# /usr/include/bits/types/time_t.h: 10

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 50
class struct_jwt(Structure):
    pass

jwt_t = struct_jwt# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 50

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 53
class struct_jwt_valid(Structure):
    pass

jwt_valid_t = struct_jwt_valid# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 53

enum_jwt_alg = c_int# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

JWT_ALG_NONE = 0# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

JWT_ALG_HS256 = (JWT_ALG_NONE + 1)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

JWT_ALG_HS384 = (JWT_ALG_HS256 + 1)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

JWT_ALG_HS512 = (JWT_ALG_HS384 + 1)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

JWT_ALG_RS256 = (JWT_ALG_HS512 + 1)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

JWT_ALG_RS384 = (JWT_ALG_RS256 + 1)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

JWT_ALG_RS512 = (JWT_ALG_RS384 + 1)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

JWT_ALG_ES256 = (JWT_ALG_RS512 + 1)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

JWT_ALG_ES384 = (JWT_ALG_ES256 + 1)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

JWT_ALG_ES512 = (JWT_ALG_ES384 + 1)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

JWT_ALG_PS256 = (JWT_ALG_ES512 + 1)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

JWT_ALG_PS384 = (JWT_ALG_PS256 + 1)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

JWT_ALG_PS512 = (JWT_ALG_PS384 + 1)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

JWT_ALG_TERM = (JWT_ALG_PS512 + 1)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

jwt_alg_t = enum_jwt_alg# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 71

jwt_malloc_t = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), c_size_t)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 88

jwt_realloc_t = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None), c_size_t)# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 89

jwt_free_t = CFUNCTYPE(UNCHECKED(None), POINTER(None))# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 90

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 96
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'jwt_key',
    'jwt_key_len',
]
struct_anon_4._fields_ = [
    ('jwt_key', POINTER(c_ubyte)),
    ('jwt_key_len', c_int),
]

jwt_key_t = struct_anon_4# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 96

jwt_key_p_t = CFUNCTYPE(UNCHECKED(c_int), POINTER(jwt_t), POINTER(jwt_key_t))# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 99

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 127
if _libs["jwt"].has("jwt_new", "cdecl"):
    jwt_new = _libs["jwt"].get("jwt_new", "cdecl")
    jwt_new.argtypes = [POINTER(POINTER(jwt_t))]
    jwt_new.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 153
if _libs["jwt"].has("jwt_decode", "cdecl"):
    jwt_decode = _libs["jwt"].get("jwt_decode", "cdecl")
    jwt_decode.argtypes = [POINTER(POINTER(jwt_t)), String, String, c_int]
    jwt_decode.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 172
for _lib in _libs.values():
    if not _lib.has("jwt_decode_2", "cdecl"):
        continue
    jwt_decode_2 = _lib.get("jwt_decode_2", "cdecl")
    jwt_decode_2.argtypes = [POINTER(POINTER(jwt_t)), String, jwt_key_p_t]
    jwt_decode_2.restype = c_int
    break

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 183
if _libs["jwt"].has("jwt_free", "cdecl"):
    jwt_free = _libs["jwt"].get("jwt_free", "cdecl")
    jwt_free.argtypes = [POINTER(jwt_t)]
    jwt_free.restype = None

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 194
if _libs["jwt"].has("jwt_dup", "cdecl"):
    jwt_dup = _libs["jwt"].get("jwt_dup", "cdecl")
    jwt_dup.argtypes = [POINTER(jwt_t)]
    jwt_dup.restype = POINTER(jwt_t)

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 221
if _libs["jwt"].has("jwt_get_grant", "cdecl"):
    jwt_get_grant = _libs["jwt"].get("jwt_get_grant", "cdecl")
    jwt_get_grant.argtypes = [POINTER(jwt_t), String]
    jwt_get_grant.restype = c_char_p

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 239
if _libs["jwt"].has("jwt_get_grant_int", "cdecl"):
    jwt_get_grant_int = _libs["jwt"].get("jwt_get_grant_int", "cdecl")
    jwt_get_grant_int.argtypes = [POINTER(jwt_t), String]
    jwt_get_grant_int.restype = c_long

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 257
if _libs["jwt"].has("jwt_get_grant_bool", "cdecl"):
    jwt_get_grant_bool = _libs["jwt"].get("jwt_get_grant_bool", "cdecl")
    jwt_get_grant_bool.argtypes = [POINTER(jwt_t), String]
    jwt_get_grant_bool.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 272
if _libs["jwt"].has("jwt_get_grants_json", "cdecl"):
    jwt_get_grants_json = _libs["jwt"].get("jwt_get_grants_json", "cdecl")
    jwt_get_grants_json.argtypes = [POINTER(jwt_t), String]
    if sizeof(c_int) == sizeof(c_void_p):
        jwt_get_grants_json.restype = ReturnString
    else:
        jwt_get_grants_json.restype = String
        jwt_get_grants_json.errcheck = ReturnString

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 292
if _libs["jwt"].has("jwt_add_grant", "cdecl"):
    jwt_add_grant = _libs["jwt"].get("jwt_add_grant", "cdecl")
    jwt_add_grant.argtypes = [POINTER(jwt_t), String, String]
    jwt_add_grant.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 311
if _libs["jwt"].has("jwt_add_grant_int", "cdecl"):
    jwt_add_grant_int = _libs["jwt"].get("jwt_add_grant_int", "cdecl")
    jwt_add_grant_int.argtypes = [POINTER(jwt_t), String, c_long]
    jwt_add_grant_int.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 330
if _libs["jwt"].has("jwt_add_grant_bool", "cdecl"):
    jwt_add_grant_bool = _libs["jwt"].get("jwt_add_grant_bool", "cdecl")
    jwt_add_grant_bool.argtypes = [POINTER(jwt_t), String, c_int]
    jwt_add_grant_bool.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 344
if _libs["jwt"].has("jwt_add_grants_json", "cdecl"):
    jwt_add_grants_json = _libs["jwt"].get("jwt_add_grants_json", "cdecl")
    jwt_add_grants_json.argtypes = [POINTER(jwt_t), String]
    jwt_add_grants_json.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 358
if _libs["jwt"].has("jwt_del_grants", "cdecl"):
    jwt_del_grants = _libs["jwt"].get("jwt_del_grants", "cdecl")
    jwt_del_grants.argtypes = [POINTER(jwt_t), String]
    jwt_del_grants.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 385
if _libs["jwt"].has("jwt_get_header", "cdecl"):
    jwt_get_header = _libs["jwt"].get("jwt_get_header", "cdecl")
    jwt_get_header.argtypes = [POINTER(jwt_t), String]
    jwt_get_header.restype = c_char_p

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 403
if _libs["jwt"].has("jwt_get_header_int", "cdecl"):
    jwt_get_header_int = _libs["jwt"].get("jwt_get_header_int", "cdecl")
    jwt_get_header_int.argtypes = [POINTER(jwt_t), String]
    jwt_get_header_int.restype = c_long

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 421
if _libs["jwt"].has("jwt_get_header_bool", "cdecl"):
    jwt_get_header_bool = _libs["jwt"].get("jwt_get_header_bool", "cdecl")
    jwt_get_header_bool.argtypes = [POINTER(jwt_t), String]
    jwt_get_header_bool.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 436
if _libs["jwt"].has("jwt_get_headers_json", "cdecl"):
    jwt_get_headers_json = _libs["jwt"].get("jwt_get_headers_json", "cdecl")
    jwt_get_headers_json.argtypes = [POINTER(jwt_t), String]
    if sizeof(c_int) == sizeof(c_void_p):
        jwt_get_headers_json.restype = ReturnString
    else:
        jwt_get_headers_json.restype = String
        jwt_get_headers_json.errcheck = ReturnString

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 456
if _libs["jwt"].has("jwt_add_header", "cdecl"):
    jwt_add_header = _libs["jwt"].get("jwt_add_header", "cdecl")
    jwt_add_header.argtypes = [POINTER(jwt_t), String, String]
    jwt_add_header.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 475
if _libs["jwt"].has("jwt_add_header_int", "cdecl"):
    jwt_add_header_int = _libs["jwt"].get("jwt_add_header_int", "cdecl")
    jwt_add_header_int.argtypes = [POINTER(jwt_t), String, c_long]
    jwt_add_header_int.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 494
if _libs["jwt"].has("jwt_add_header_bool", "cdecl"):
    jwt_add_header_bool = _libs["jwt"].get("jwt_add_header_bool", "cdecl")
    jwt_add_header_bool.argtypes = [POINTER(jwt_t), String, c_int]
    jwt_add_header_bool.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 508
if _libs["jwt"].has("jwt_add_headers_json", "cdecl"):
    jwt_add_headers_json = _libs["jwt"].get("jwt_add_headers_json", "cdecl")
    jwt_add_headers_json.argtypes = [POINTER(jwt_t), String]
    jwt_add_headers_json.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 522
if _libs["jwt"].has("jwt_del_headers", "cdecl"):
    jwt_del_headers = _libs["jwt"].get("jwt_del_headers", "cdecl")
    jwt_del_headers.argtypes = [POINTER(jwt_t), String]
    jwt_del_headers.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 553
if _libs["jwt"].has("jwt_dump_fp", "cdecl"):
    jwt_dump_fp = _libs["jwt"].get("jwt_dump_fp", "cdecl")
    jwt_dump_fp.argtypes = [POINTER(jwt_t), POINTER(FILE), c_int]
    jwt_dump_fp.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 573
if _libs["jwt"].has("jwt_dump_str", "cdecl"):
    jwt_dump_str = _libs["jwt"].get("jwt_dump_str", "cdecl")
    jwt_dump_str.argtypes = [POINTER(jwt_t), c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        jwt_dump_str.restype = ReturnString
    else:
        jwt_dump_str.restype = String
        jwt_dump_str.errcheck = ReturnString

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 587
for _lib in _libs.values():
    if not _lib.has("jwt_dump_grants_str", "cdecl"):
        continue
    jwt_dump_grants_str = _lib.get("jwt_dump_grants_str", "cdecl")
    jwt_dump_grants_str.argtypes = [POINTER(jwt_t), c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        jwt_dump_grants_str.restype = ReturnString
    else:
        jwt_dump_grants_str.restype = String
        jwt_dump_grants_str.errcheck = ReturnString
    break

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 600
if _libs["jwt"].has("jwt_encode_fp", "cdecl"):
    jwt_encode_fp = _libs["jwt"].get("jwt_encode_fp", "cdecl")
    jwt_encode_fp.argtypes = [POINTER(jwt_t), POINTER(FILE)]
    jwt_encode_fp.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 613
if _libs["jwt"].has("jwt_encode_str", "cdecl"):
    jwt_encode_str = _libs["jwt"].get("jwt_encode_str", "cdecl")
    jwt_encode_str.argtypes = [POINTER(jwt_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        jwt_encode_str.restype = ReturnString
    else:
        jwt_encode_str.restype = String
        jwt_encode_str.errcheck = ReturnString

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 621
if _libs["jwt"].has("jwt_free_str", "cdecl"):
    jwt_free_str = _libs["jwt"].get("jwt_free_str", "cdecl")
    jwt_free_str.argtypes = [String]
    jwt_free_str.restype = None

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 650
if _libs["jwt"].has("jwt_set_alg", "cdecl"):
    jwt_set_alg = _libs["jwt"].get("jwt_set_alg", "cdecl")
    jwt_set_alg.argtypes = [POINTER(jwt_t), jwt_alg_t, POINTER(c_ubyte), c_int]
    jwt_set_alg.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 660
if _libs["jwt"].has("jwt_get_alg", "cdecl"):
    jwt_get_alg = _libs["jwt"].get("jwt_get_alg", "cdecl")
    jwt_get_alg.argtypes = [POINTER(jwt_t)]
    jwt_get_alg.restype = jwt_alg_t

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 671
if _libs["jwt"].has("jwt_alg_str", "cdecl"):
    jwt_alg_str = _libs["jwt"].get("jwt_alg_str", "cdecl")
    jwt_alg_str.argtypes = [jwt_alg_t]
    jwt_alg_str.restype = c_char_p

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 684
if _libs["jwt"].has("jwt_str_alg", "cdecl"):
    jwt_str_alg = _libs["jwt"].get("jwt_str_alg", "cdecl")
    jwt_str_alg.argtypes = [String]
    jwt_str_alg.restype = jwt_alg_t

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 718
if _libs["jwt"].has("jwt_set_alloc", "cdecl"):
    jwt_set_alloc = _libs["jwt"].get("jwt_set_alloc", "cdecl")
    jwt_set_alloc.argtypes = [jwt_malloc_t, jwt_realloc_t, jwt_free_t]
    jwt_set_alloc.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 727
if _libs["jwt"].has("jwt_get_alloc", "cdecl"):
    jwt_get_alloc = _libs["jwt"].get("jwt_get_alloc", "cdecl")
    jwt_get_alloc.argtypes = [POINTER(jwt_malloc_t), POINTER(jwt_realloc_t), POINTER(jwt_free_t)]
    jwt_get_alloc.restype = None

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 755
if _libs["jwt"].has("jwt_validate", "cdecl"):
    jwt_validate = _libs["jwt"].get("jwt_validate", "cdecl")
    jwt_validate.argtypes = [POINTER(jwt_t), POINTER(jwt_valid_t)]
    jwt_validate.restype = c_uint

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 769
if _libs["jwt"].has("jwt_valid_new", "cdecl"):
    jwt_valid_new = _libs["jwt"].get("jwt_valid_new", "cdecl")
    jwt_valid_new.argtypes = [POINTER(POINTER(jwt_valid_t)), jwt_alg_t]
    jwt_valid_new.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 780
if _libs["jwt"].has("jwt_valid_free", "cdecl"):
    jwt_valid_free = _libs["jwt"].get("jwt_valid_free", "cdecl")
    jwt_valid_free.argtypes = [POINTER(jwt_valid_t)]
    jwt_valid_free.restype = None

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 792
if _libs["jwt"].has("jwt_valid_get_status", "cdecl"):
    jwt_valid_get_status = _libs["jwt"].get("jwt_valid_get_status", "cdecl")
    jwt_valid_get_status.argtypes = [POINTER(jwt_valid_t)]
    jwt_valid_get_status.restype = c_uint

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 800
for _lib in _libs.values():
    if not _lib.has("jwt_valid_get_nbf_leeway", "cdecl"):
        continue
    jwt_valid_get_nbf_leeway = _lib.get("jwt_valid_get_nbf_leeway", "cdecl")
    jwt_valid_get_nbf_leeway.argtypes = [POINTER(jwt_valid_t)]
    jwt_valid_get_nbf_leeway.restype = time_t
    break

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 808
for _lib in _libs.values():
    if not _lib.has("jwt_valid_get_exp_leeway", "cdecl"):
        continue
    jwt_valid_get_exp_leeway = _lib.get("jwt_valid_get_exp_leeway", "cdecl")
    jwt_valid_get_exp_leeway.argtypes = [POINTER(jwt_valid_t)]
    jwt_valid_get_exp_leeway.restype = time_t
    break

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 823
if _libs["jwt"].has("jwt_valid_add_grant", "cdecl"):
    jwt_valid_add_grant = _libs["jwt"].get("jwt_valid_add_grant", "cdecl")
    jwt_valid_add_grant.argtypes = [POINTER(jwt_valid_t), String, String]
    jwt_valid_add_grant.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 841
if _libs["jwt"].has("jwt_valid_get_grant", "cdecl"):
    jwt_valid_get_grant = _libs["jwt"].get("jwt_valid_get_grant", "cdecl")
    jwt_valid_get_grant.argtypes = [POINTER(jwt_valid_t), String]
    jwt_valid_get_grant.restype = c_char_p

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 855
if _libs["jwt"].has("jwt_valid_add_grant_int", "cdecl"):
    jwt_valid_add_grant_int = _libs["jwt"].get("jwt_valid_add_grant_int", "cdecl")
    jwt_valid_add_grant_int.argtypes = [POINTER(jwt_valid_t), String, c_long]
    jwt_valid_add_grant_int.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 873
if _libs["jwt"].has("jwt_valid_get_grant_int", "cdecl"):
    jwt_valid_get_grant_int = _libs["jwt"].get("jwt_valid_get_grant_int", "cdecl")
    jwt_valid_get_grant_int.argtypes = [POINTER(jwt_valid_t), String]
    jwt_valid_get_grant_int.restype = c_long

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 892
if _libs["jwt"].has("jwt_valid_add_grant_bool", "cdecl"):
    jwt_valid_add_grant_bool = _libs["jwt"].get("jwt_valid_add_grant_bool", "cdecl")
    jwt_valid_add_grant_bool.argtypes = [POINTER(jwt_valid_t), String, c_int]
    jwt_valid_add_grant_bool.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 910
if _libs["jwt"].has("jwt_valid_get_grant_bool", "cdecl"):
    jwt_valid_get_grant_bool = _libs["jwt"].get("jwt_valid_get_grant_bool", "cdecl")
    jwt_valid_get_grant_bool.argtypes = [POINTER(jwt_valid_t), String]
    jwt_valid_get_grant_bool.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 922
if _libs["jwt"].has("jwt_valid_add_grants_json", "cdecl"):
    jwt_valid_add_grants_json = _libs["jwt"].get("jwt_valid_add_grants_json", "cdecl")
    jwt_valid_add_grants_json.argtypes = [POINTER(jwt_valid_t), String]
    jwt_valid_add_grants_json.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 936
if _libs["jwt"].has("jwt_valid_get_grants_json", "cdecl"):
    jwt_valid_get_grants_json = _libs["jwt"].get("jwt_valid_get_grants_json", "cdecl")
    jwt_valid_get_grants_json.argtypes = [POINTER(jwt_valid_t), String]
    if sizeof(c_int) == sizeof(c_void_p):
        jwt_valid_get_grants_json.restype = ReturnString
    else:
        jwt_valid_get_grants_json.restype = String
        jwt_valid_get_grants_json.errcheck = ReturnString

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 950
if _libs["jwt"].has("jwt_valid_del_grants", "cdecl"):
    jwt_valid_del_grants = _libs["jwt"].get("jwt_valid_del_grants", "cdecl")
    jwt_valid_del_grants.argtypes = [POINTER(jwt_valid_t), String]
    jwt_valid_del_grants.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 962
if _libs["jwt"].has("jwt_valid_set_now", "cdecl"):
    jwt_valid_set_now = _libs["jwt"].get("jwt_valid_set_now", "cdecl")
    jwt_valid_set_now.argtypes = [POINTER(jwt_valid_t), time_t]
    jwt_valid_set_now.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 972
for _lib in _libs.values():
    if not _lib.has("jwt_valid_set_nbf_leeway", "cdecl"):
        continue
    jwt_valid_set_nbf_leeway = _lib.get("jwt_valid_set_nbf_leeway", "cdecl")
    jwt_valid_set_nbf_leeway.argtypes = [POINTER(jwt_valid_t), time_t]
    jwt_valid_set_nbf_leeway.restype = c_int
    break

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 982
for _lib in _libs.values():
    if not _lib.has("jwt_valid_set_exp_leeway", "cdecl"):
        continue
    jwt_valid_set_exp_leeway = _lib.get("jwt_valid_set_exp_leeway", "cdecl")
    jwt_valid_set_exp_leeway.argtypes = [POINTER(jwt_valid_t), time_t]
    jwt_valid_set_exp_leeway.restype = c_int
    break

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 997
if _libs["jwt"].has("jwt_valid_set_headers", "cdecl"):
    jwt_valid_set_headers = _libs["jwt"].get("jwt_valid_set_headers", "cdecl")
    jwt_valid_set_headers.argtypes = [POINTER(jwt_valid_t), c_int]
    jwt_valid_set_headers.restype = c_int

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 1012
for _lib in _libs.values():
    if not _lib.has("jwt_exception_str", "cdecl"):
        continue
    jwt_exception_str = _lib.get("jwt_exception_str", "cdecl")
    jwt_exception_str.argtypes = [c_uint]
    if sizeof(c_int) == sizeof(c_void_p):
        jwt_exception_str.restype = ReturnString
    else:
        jwt_exception_str.restype = String
        jwt_exception_str.errcheck = ReturnString
    break

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 73
try:
    JWT_ALG_INVAL = JWT_ALG_TERM
except:
    pass

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 76
try:
    JWT_VALIDATION_SUCCESS = 0x0000
except:
    pass

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 77
try:
    JWT_VALIDATION_ERROR = 0x0001
except:
    pass

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 78
try:
    JWT_VALIDATION_ALG_MISMATCH = 0x0002
except:
    pass

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 79
try:
    JWT_VALIDATION_EXPIRED = 0x0004
except:
    pass

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 80
try:
    JWT_VALIDATION_TOO_NEW = 0x0008
except:
    pass

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 81
try:
    JWT_VALIDATION_ISS_MISMATCH = 0x0010
except:
    pass

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 82
try:
    JWT_VALIDATION_SUB_MISMATCH = 0x0020
except:
    pass

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 83
try:
    JWT_VALIDATION_AUD_MISMATCH = 0x0040
except:
    pass

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 84
try:
    JWT_VALIDATION_GRANT_MISSING = 0x0080
except:
    pass

# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 85
try:
    JWT_VALIDATION_GRANT_MISMATCH = 0x0100
except:
    pass

jwt = struct_jwt# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 50

jwt_valid = struct_jwt_valid# /home/bluecmd/Downloads/libjwt-1.17.2/include/jwt.h: 53

# No inserted files

# No prefix-stripping

