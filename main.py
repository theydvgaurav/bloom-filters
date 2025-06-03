import hashlib


class BloomFilter:
    def __init__(self):
        self._ds = [0 for i in range(11)]

    def _set_ith_bit(self, i):
        self._ds[i] = 1

    def _check_ith_bit(self, i):
        return self._ds[i]

    @staticmethod
    def _hash_to_digits(key):
        algorithms = ['md5', 'sha1', 'sha256']
        results = []
        for algo in algorithms:
            hash_func = getattr(hashlib, algo)
            hash_bytes = hash_func(key.encode()).digest()
            hash_int = int.from_bytes(hash_bytes, 'big')
            results.append(hash_int % 10)
        return results

    def add(self, key):
        for idx in self._hash_to_digits(key):
            self._set_ith_bit(idx)

    def search(self, key):
        return all({self._check_ith_bit(idx) for idx in self._hash_to_digits(key)})


if __name__ == "__main__":
    bf = BloomFilter()
    bf.add("Gaurav")
    print(bf.search("Abhinav"))
    print(bf.search("Gaurav"))
