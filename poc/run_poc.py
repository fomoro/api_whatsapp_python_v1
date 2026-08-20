"""Ejecuta el POC preservado sin modificar sus importaciones internas."""

from pathlib import Path
from importlib import import_module
import sys
import types


def register_legacy_package() -> None:
    """Mantiene compatible la importación histórica ``old.database``."""
    legacy_package = types.ModuleType("old")
    legacy_package.__path__ = [str(Path(__file__).resolve().parent / "poc")]
    legacy_package.__package__ = "old"
    sys.modules.setdefault("old", legacy_package)


def main() -> None:
    register_legacy_package()
    poc_app = import_module("poc.app")
    poc_app.app.run(host="0.0.0.0", port=80, debug=True)


if __name__ == "__main__":
    main()
