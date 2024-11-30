from klein import Klein

bosun_api_klein = Klein()

class BosunAPI(object):
    @classmethod
    def configure(cls, _):
        return cls()

    def __register_jobs(self, register_fn):
        return
        register_fn(self.run)

    def register_hooks(self, register_fn):
        register_fn("bosun:register_jobs", self.__register_jobs)
        pass

    async def run(self):
        bosun_api_klein.run("localhost",8122)

    @bosun_api_klein.route('/')
    async def testing(request):
        return("hi there")
