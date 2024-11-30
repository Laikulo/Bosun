class BosunManager(object):
    
    @classmethod
    def configure(cls, _):
        return cls()

    def __register_jobs(self, register_fn):
        register_fn(self.run)

    def register_hooks(self, register_fn):
        register_fn("bosun:register_jobs", self.__register_jobs)
        pass

    async def run(self):
        pass

# vim: set et sts=4 sw=4 ts=4:
