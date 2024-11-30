from typing import Dict, List, Any, Callable
from pprint import pprint as pp
import asyncio

class Bosun(object):
    def __init__(self):
        self._hooks: Dict[str,List[Any]] = {}

    def entrypoint(self):
        from .klippy_host import KlippyHost
        KlippyHost.configure(None).register_hooks(self._register_hook)

        from .manager import BosunManager
        BosunManager.configure(None).register_hooks(self._register_hook)

        from .api import BosunAPI
        BosunAPI.configure(None).register_hooks(self._register_hook)

        self._process_hooks('bosun:system_startup')

        initial_jobs = []

        def register_fn(fn: callable):
            initial_jobs.append(fn)

        self._process_hooks('bosun:register_jobs', {
            'register_fn': register_fn
        })

        pp(initial_jobs)

        asyncio.run(self.startup(initial_jobs))


    async def startup(self, initial_jobs):
        results = await asyncio.gather(*[x() for x in initial_jobs])
        pp(results.resolve())
        

    def _register_hook(self, hook_type: str, hook: Callable):
        if not hook_type in  self._hooks:
            self._hooks[hook_type] = []
        self._hooks[hook_type].append(hook)

    def _process_hooks(self, hook_type: str, args: Dict[str, Any] = {}):
        if hook_type in self._hooks:
            for hook in self._hooks[hook_type]:
                hook(**args)

    @classmethod
    def run(cls):
        instance = cls()
        return instance.entrypoint()
# vi: set sts=4 sw=4 ts=4 et: 
