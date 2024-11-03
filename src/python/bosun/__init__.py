from typing import Dict, List, Any, Callable

class Bosun(object):
    def __init__(self):
        self._hooks: Dict[str,List[Any]] = {}

    def entrypoint(self):
        # Locate components, and register their hooks
        from .klippy_host import KlippyHost
        KlippyHost().setup_env()
        self._process_hooks('bosun:system_startup')

    def _register_hook(self, hook_type: str, hook: Callable):
        if not hook_type in  self._hooks:
            self._hooks[hook_type] = []
        self._hooks[hook_type].append(hook)

    def _process_hooks(self, hook_type: str, args: Dict[str, Any] = []):
        if hook_type in self._hooks:
            for hook in self._hooks[hook_type]:
                hook(**args)

    @classmethod
    def run(cls):
        instance = cls()
        return instance.entrypoint()