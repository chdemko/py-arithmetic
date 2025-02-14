"""Script for th generation of compiled modules using Cython."""

import shutil
from pathlib import Path
from typing import Any

from Cython.Build import cythonize
from Cython.Distutils import build_ext
from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from setuptools import Distribution, Extension


class CustomBuildHook(BuildHookInterface):
    """
    Custom build hook.
    """

    def initialize(
        self,
        version: str,  # noqa: ARG002
        build_data: dict[str, Any],
    ) -> None:
        """
        Initialize the building.

        Parameters
        ----------
        version
            The verion ben built
        build_data
            The building data
        """
        build_data["pure_python"] = False
        build_data["infer_tag"] = True

        extensions = [
            Extension(
                "*",
                ["src/arithmetic/*.pyx"],
            ),
        ]

        ext_modules = cythonize(
            extensions,
            compiler_directives={"binding": True, "language_level": 3},
        )

        distribution = Distribution({"ext_modules": ext_modules})

        cmd = build_ext(distribution)
        cmd.ensure_finalized()
        cmd.run()

        # Copy built extensions back to the project
        for output in cmd.get_outputs():
            output_path = Path(output)
            relative_extension = Path("src", output_path.relative_to(cmd.build_lib))
            shutil.copyfile(output, relative_extension)
            relative_extension.chmod(output_path.stat().st_mode)
