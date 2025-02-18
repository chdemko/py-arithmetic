"""Script for th generation of compiled modules using Cython."""

import shutil
from collections.abc import Iterable
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

    @classmethod
    def _get_directories(cls) -> Iterable[Path]:
        return [
            Path("src", "arithmetic"),
        ]

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
            The version been built
        build_data
            The building data
        """
        build_data["artifacts"] = ["src/**/*.so"]
        build_data["pure_python"] = False
        build_data["infer_tag"] = True

        # Cleanup project
        self._clean()

        # Getting cython files
        extensions = [
            Extension("*", [Path(directory, "*.pyx")])
            for directory in self._get_directories()
        ]

        # Cythonize modules
        ext_modules = cythonize(
            extensions,
            compiler_directives={"binding": True, "language_level": 3},
        )

        # Get a distribution
        distribution = Distribution({"ext_modules": ext_modules})

        # Build the distribution
        cmd = build_ext(distribution)
        cmd.ensure_finalized()
        cmd.run()

        # Copy built extensions back to the project
        for output in cmd.get_outputs():
            output_path = Path(output)
            relative_extension = Path("src", output_path.relative_to(cmd.build_lib))
            shutil.copyfile(output, relative_extension)
            relative_extension.chmod(output_path.stat().st_mode)

    def _clean(self, *, complete: bool = False) -> None:
        """
        Clean up.

        Parameters
        ----------
        complete
            Remove also .c files

        """
        for directory in self._get_directories():
            for file in directory.glob("*.pyx"):
                if complete:
                    file.with_suffix(".c").unlink(missing_ok=True)
                for so_file in directory.glob(f"{file.stem}*.so"):
                    so_file.unlink()

    def clean(self, versions: Iterable[str]) -> None:  # noqa: ARG002
        """
        Clean up.

        Parameters
        ----------
        versions
            An iterable of string

        """
        self._clean(complete=True)
