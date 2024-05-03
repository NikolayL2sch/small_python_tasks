from re import fullmatch


class Field(dict):

    @staticmethod
    def normalise_key(key):
        if isinstance(key, tuple):
            key = str(key[0]) + str(key[1])
        key = ''.join(sorted(key.lower()))
        return key

    @staticmethod
    def check_key(key):
        if not (isinstance(key, str) or isinstance(key, tuple)):
            raise TypeError
        elif isinstance(key, tuple) and len(key) != 2:
            raise ValueError
        normalised_key = Field.normalise_key(key)
        regexs = (r"^[A-Za-z]{1}\d+$", r"^\d+[A-Za-z]{1}$")
        if fullmatch(regexs[0], normalised_key) is None and fullmatch(regexs[1], normalised_key) is None:
            raise ValueError
        return normalised_key

    def __getitem__(self, key):
        try:
            return super(Field, self).__getitem__(Field.check_key(key))
        except KeyError:
            return None
        except ValueError:
            normalised_key = self.normalise_key(key)
            if key == '_iter_values':
                normalised_key = key
            try:
                return super(Field, self).__getitem__(normalised_key)
            except KeyError:
                raise ValueError

    def __setitem__(self, key, value):
        super(Field, self).__setitem__(Field.check_key(key), value)

    def __contains__(self, key):
        return Field.check_key(key) in super(Field, self).keys()

    def __delitem__(self, key):
        super(Field, self).__delitem__(Field.check_key(key))

    def __iter__(self):
        self._iter_values = iter(list(super(Field, self).values()))
        return self

    def __next__(self):
        try:
            return next(self._iter_values)
        except StopIteration:
            del self._iter_values
            raise StopIteration

    def __getattr__(self, attr):
        try:
            return super(Field, self).__getattribute__(attr)
        except AttributeError:
            return self.__getitem__(attr)

    def __setattr__(self, name, value):
        try:
            normalised_key = self.check_key(name)
            self.__setitem__(normalised_key, value)
        except:
            normalised_key = self.normalise_key(name)
        self.__dict__[name] = value

    def __delattr__(self, name):
        try:
            del self.__dict__[name]
        except KeyError:
            self.__delitem__(name)


field = Field()
field['a', 1] = 100
del field.a1
