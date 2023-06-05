class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key):
        index = self._hash_function(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                return

        bucket.append([key])

    def get(self, key):
        index = self._hash_function(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[0]

        return None

    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.table[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return

    def display(self):
        with open("resultados/hash_table.txt", "w") as file:
            for index, bucket in enumerate(self.table):
                file.write(f"Index {index}: ")
                for pair in bucket:
                    file.write(f"{pair[0]} ")
                file.write("\n")

    