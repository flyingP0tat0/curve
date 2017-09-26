import cx_freeze

executables = [cx_freeze.Executable("../src/main.py")]

cx_freeze.setup(
  name = "Curve",
  description = "Curve game",
  version = "0.1.0",
  executables = executables,
  options = {
    "build_exe": {
      "packages": ["os", "threading", "math", "random", "yaml", "pygame", "ws4py"],
      "include_files": ["../config/config.yml", "../config/color.yml"],
      "optimize": 2,
      "compress": True
    }
  }
)
