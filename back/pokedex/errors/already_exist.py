class AlreadyExistError(Exception):
    def __init__(self, resource, resource_id):
        Exception.__init__(self)
        self.resource = resource
        self.resource_id = resource_id

class CollectionAlreadyExistError(AlreadyExistError):
    def __init__(self, resource_id):
        AlreadyExistError.__init__(self, "Collection", resource_id)