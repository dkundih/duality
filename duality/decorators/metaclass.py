# makes multiple instances of the object available.
class Meta(type):

    def __call__(
        self, 
        *args, 
        **kwargs,
        ) -> object:
        instance = super(Meta, self).__call__(*args, **kwargs)

        return instance

    def __init__(
        self, 
        name, 
        base, 
        attr,
        ) -> object:
        super(Meta, self).__init__(name, base, attr)
