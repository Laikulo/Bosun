from typing import Dict, List, Any, Callable

class Bosun(object):
    def __init__(self):
        self._hooks = Dict[str,List[Any]]

    def entrypoint():
        # Locate components, and register their hooks

        _process_hooks('bosun:system_startup')

    def _register_hook(hook_type: str, hook: Callable):
        if not self._hooks[hook_type]:
            self._hooks[hook_type] = []
        self._hooks[hook_type].append(hook)

    def _process_hooks(hook_type: str, args: Dict[str, Any] = []):
        if self._hooks[hook_type]:
            for hook in self._hooks[hook_type]:
                hook(**args)

    @classmethod
    def run(cls):
        instance = cls()
        return instance.entrypoint()



if __name__ == "__main__":
    Bosun.run()