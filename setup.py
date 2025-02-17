import os
import sys
import platform
import setuptools


# # --- Detect if extensions should be disabled ------------------------------

wrapt_env = os.environ.get('WRAPT_INSTALL_EXTENSIONS')

if wrapt_env is None:
    wrapt_env = os.environ.get('WRAPT_EXTENSIONS')

if wrapt_env is not None:
    disable_extensions = wrapt_env.lower() == 'false'
    force_extensions = wrapt_env.lower() == 'true'
else:
    if platform.system() == 'Windows' and sys.version_info[0] < 3:
      disable_extensions = True
      force_extensions = False
    else:
      disable_extensions = False
      force_extensions = False

if platform.python_implementation() != "CPython":
    disable_extensions = True

# --- C extension ------------------------------------------------------------

extensions = [
    setuptools.Extension(
        "matrix_wrapt._wrappers",
        sources=["src/matrix_wrapt/_wrappers.c"],
        optional=not force_extensions,
    )
]


# --- Setup ------------------------------------------------------------------

setuptools.setup(
    ext_modules=[] if disable_extensions else extensions
)
