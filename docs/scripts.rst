.. title:: Scripts

Scripts
=======

This page describes the `retdec-python <https://github.com/s3rvac/retdec-python>`_ scripts and their usage.

Currently, there are two scripts: ``decompiler`` and ``fileinfo``. They provide access to the `decompilation <https://retdec.com/api/docs/decompiler.html>`_ and `file-analyzing <https://retdec.com/api/docs/fileinfo.html>`_ services, respectively.

Authentication
--------------

The scripts need to authenticate you to `retdec.com <https://retdec.com>`_. To specify your API key, either use the ``-k KEY`` or ``--api-key KEY`` parameter:

.. code::

    $ decompiler -k YOUR-API-KEY file.exe

or set the ``RETDEC_API_KEY`` environment variable:

.. code::

    $ export RETDEC_API_KEY=YOUR-API-KEY
    $ decompiler file.exe

An advantage of the environment variable is that you do not have to specify the API key every time you run a script.

.. _decompiler:

Decompiler
----------

The ``decompiler`` script provides access to the `decompilation service <https://retdec.com/api/docs/decompiler.html>`_. It allows you to decompile binary files into a high-level language representation, such as C.

Usage
^^^^^
.. code::

    $ decompiler [OPTIONS] FILE

Output files are stored into the same directory where the input file is located. For example, if the input file is ``dir/prog.exe``, then the decompiled code in the C language is saved as ``dir/prog.c``. You can override the output directory by using the ``-o/--output-dir`` parameter.

Options
^^^^^^^

See the `official documentation <https://retdec.com/api/docs/decompiler.html#decompilation-parameters>`_ for more details.

* ``-a ARCH``, ``--architecture ARCH`` -- Architecture to force when (de)compiling. Supported architectures: ``x86``, ``arm``, ``thumb``, ``mips``, ``pic32``, ``powerpc``.
* ``-b``, ``--brief`` -- Print fewer information during the decompilation.
* ``-c COMPILER``, ``--compiler COMPILER`` -- Compiler to use when compiling input C source files. Supported compilers: ``gcc``, ``clang``.
* ``-C LEVEL``, ``--compiler-optimizations LEVEL`` -- Optimization level to use when compiling input C source files. Supported levels: ``O0``, ``O1``, ``O2``, ``O3``.
* ``--endian`` -- Endianness of the machine code (``bin`` and ``raw`` modes only). Supported endians: ``little``, ``big``.
* ``-f FORMAT``, ``--file-format FORMAT`` -- File format to force when compiling input C source files. Supported formats: ``elf``, ``pe``.
* ``-g``, ``--compiler-debug`` -- Compile the input C file with debugging information (i.e. passes the ``-g`` flag to the used compiler).
* ``-s``, ``--compiler-strip`` -- Strip the compiled C file prior its decompilation.
* ``-k KEY``, ``--api-key KEY`` -- Specifies the API key to be used.
* ``-l LANGUAGE``, ``--target-language LANGUAGE`` -- Target high-level language. Supported languages: ``c``, ``py``.
* ``--graph-format FORMAT`` -- Format of the generated call and control-flow graphs. Supported formats: ``png``, ``svg``, ``pdf``.
* ``-m MODE``, ``--mode MODE`` -- Decompilation mode. `Supported modes <https://retdec.com/api/docs/decompiler.html#decompilation-modes>`_: ``bin``, ``c``, and ``raw``. By default, the script performs an automatic detection based on the extension of the input file.
* ``-o DIR``, ``--output-dir DIR`` -- Save the outputs into this directory.
* ``-p FILE``, ``--pdb-file`` -- PDB file associated with the input file.
* ``-q``, ``--quiet`` -- Print only errors, nothing else (not even progress).
* ``-V``, ``--version`` -- Print the script and library version.
* ``--var-names STYLE`` -- Naming style for variables. Supported styles: ``readable``, ``address``, ``hungarian``, ``simple``, and ``unified``.
* ``-O LEVEL``, ``--optimizations LEVEL`` -- Level of optimizations performed by the decompiler. Supported levels: ``none``, ``limited``, ``normal``, and ``aggressive``.
* ``-K``, ``--keep-unreach-funcs`` -- Decompile all functions, even if they are not reachable.
* ``--only-funcs`` -- Decompile only the given functions (a comma-separated list of function names, e.g. ``func1,func2``).
* ``--only-ranges'`` -- Decompile only the given address ranges (a comma-separated list of address ranges, e.g. ``0x100-0x200,0x500-0x600``).
* ``--decoding`` -- What should be decoded in a selective decompilation? Supported types: ``everything``, ``only``.
* ``--no-addresses`` -- Disable the emission of addresses in comments in the generated code.
* ``--raw-entry-point`` -- Virtual memory address where execution flow should start in the machine code (``raw`` mode only).
* ``--raw-section-vma`` -- Address where the section created from the machine code will be placed in virtual memory (``raw`` mode only).
* ``--ar-index`` -- Index of the object file in the input archive to be decompiled when decompiling an archive.
* ``--ar-name`` -- Name of the object file in the input archive to be decompiled when decompiling an archive.
* ``--with-cg`` -- Generate a call graph when the decompilation ends.
* ``--with-cfgs`` -- Generate call graphs for all functions when the decompilation ends.
* ``--with-archive`` -- Generate an archive containing all decompilation outputs when the decompilation ends.

Example
^^^^^^^

.. code::

    $ decompiler -k YOUR-API-KEY file.exe

    v23bmYb67R
    ----------

    Waiting for resources (0%)...                      [OK]
    Pre-Processing:
        Obtaining file information (5%)...             [OK]
        Unpacking (10%)...                             [OK]
    Front-End:
        Initializing (20%)...                          [OK]
    [..]
    Done (100%)...

    Downloading:
     - file.c

``file.c`` then contains the decompiled C code.

.. _fileinfo:

Fileinfo
--------

The ``fileinfo`` script provides access to the `file-analyzing service <https://retdec.com/api/docs/fileinfo.html>`_. It allows you to obtain information about binary files.

Usage
^^^^^
.. code::

    $ fileinfo [OPTIONS] FILE

Options
^^^^^^^

* ``-k KEY``, ``--api-key KEY`` -- Specifies the API key to be used.
* ``-f FORMAT``, ``--output-format`` -- Format in which the output should be printed. Available formats are ``plain`` (plain text; the default) and ``json`` (`JSON <https://en.wikipedia.org/wiki/JSON>`_).
* ``-v``, ``--verbose`` -- Print all available information about the file.
* ``-V``, ``--version`` -- Print the script and library version.

Example
^^^^^^^

.. code::

    $ fileinfo -k YOUR-API-KEY file.exe

    Input file               : file.exe
    File format              : PE
    File class               : 32-bit
    File type                : Executable file
    Architecture             : x86 (or later and compatible)
    Endianness               : Little endian
    Entry point address      : 0x4014e0
    Entry point offset       : 0x8e0
    Entry point section name : .text
    Entry point section index: 0
    Bytes on entry point     : 31ed5e89e183e4f05054526860c1040868f0c00408515668
    Detected compiler/packer : GCC (x86_64-unknown-linux-gnu) (4.7.2) (100%)
