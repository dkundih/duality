# makes multiple instances of the object available.
class Meta(type):

    def __call__(self, *args, **kwargs):
        instance = super(Meta, self).__call__(*args, **kwargs)
        return instance
    def __init__(self, name, base, attr):
        super(Meta, self).__init__(name, base, attr)
