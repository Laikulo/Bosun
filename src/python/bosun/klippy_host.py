from pathlib import Path
from os import PathLike

from dataclass import dataclass

class KlippyHost(object):

    def setup_env(self):



class KlippyConfig(object):
    def __init__



class KlippyHostProcessConfig(object):
    """
    Represents the configuration of a klippy host
    """
    def __init__(self):
        self.config_path: Optional[PathLike] = None
        self.input_tty_path: Optional[PathLike] = None
        self.api_socket_path: Optional[PathLike] = None
        self.log_path: Optional[PathLike] = None
        self.verbose: bool = False

        self.extra_args: List[str] = []

    def validate(self):
        if not config_path:
            raise ValueError("Printer configuration path was unspecified")

    def startup_args(self):
        self.validate()
        startup_args = []

        if self.input_tty_path:
            startup_args += ['-I', input_tty_path]

        if self.api_socket_path:
            startup_args += ['-a', api_socket_path]

        if self.log_path:
            startup_args += ['-l', log_path]

        if self.verbose:
            startup_args.append('-v')

        if self.config_path:
            startup_args.append(self.config_path)

        if self.extra_args:
            startup.args += extra_args
        
        return startup_args
