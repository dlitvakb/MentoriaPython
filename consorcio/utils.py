def is_subclass(klass, super_class):
    try:
        return issubclass(klass, super_class) and not klass is super_class
    except:
        return False
