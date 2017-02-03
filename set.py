from hashtable import HashTable


class Set(HashTable):
    def __init__(self, init_size=8):
        super(Set, self).__init__()

    def bucket_index(self, key):
        return super.bucket_index(super.self, key)

    def length(self):
        # TODO: Count number of key-value entries in each of the buckets
        length = 0
        for bucket in self.buckets:
            length += bucket.length()
        return length

    def contains(self, key):
        return super.contains(super.self, key)

    def get(self, key):
        return super.get(super.self, key)

    def set(self, key, value):
        return super.set(super.self, key, value)

    def delete(self, key):
        super.delete(super.self, key)

    def keys(self):
        return super.keys(self.super)
