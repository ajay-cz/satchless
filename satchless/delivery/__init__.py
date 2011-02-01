class DeliveryProvider(object):
    def enum_types(self, customer, delivery_group=None):
        '''
        Should return an iterable consisting of pairs suitable for a select
        widget. When given a DeliveryGroup it should only return types
        available for that group.
        '''
        raise NotImplemented()

    def get_form(self, customer, delivery_group, typ):
        '''
        If applicable, return a form class responsible for getting any
        additional delivery data.
        '''
        return None

    def get_variant(self, customer, delivery_group, typ, form):
        '''
        Take a valid form instance if any and return a DeliveryVariant instance.
        '''
        raise NotImplemented()
