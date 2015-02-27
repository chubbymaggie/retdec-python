#!/usr/bin/env python
#
# A script for decompiling files by using the retdec.com public REST API
# (https://retdec.com/api/). Internally, it uses the retdec-python library
# (https://github.com/s3rvac/retdec-python), which is assumed to be installed
# and available for import.
#
# Copyright: (c) 2015 by Petr Zemek <s3rvac@gmail.com> and contributors
# License: MIT, see the LICENSE file for more details
#

import sys

# Allow running the script from the root repository path, i.e. by executing
# `scripts/decompile.py`. If we did not include the current working
# directory into the path, the 'retdec' package would not be found.
sys.path.append('.')

try:
    from retdec.tools import decompile
except ImportError:
    sys.stderr.write(
        "error: Failed to import 'retdec'."
        ' Make sure that you have retdec-python installed'
        ' (https://github.com/s3rvac/retdec-python).\n'
    )
    sys.exit(1)

if __name__ == '__main__':
    sys.exit(decompile.main())
