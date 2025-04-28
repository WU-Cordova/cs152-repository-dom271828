import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets: Array[LinkedList[Tuple[KT, VT]]] = \
            Array(starting_sequence=[LinkedList(data_type=tuple) for _ in range(number_of_buckets)],
                data_type=LinkedList)
    
        self._count: int = 0
        self._capacity: int = 7
        self._load_factor: float = load_factor
        self._hash_function = custom_hash_function or self._default_hash_function

    def _get_bucket_number(self, key: KT, bucket_size: int):
        print(key)
        bucket_index = self._hash_function(key)
        return bucket_index % bucket_size

    @staticmethod
    def _next_prime(n: int) -> int:

        def is_prime(wow: int) -> bool:
            for i in range(wow):
                if i % wow == 0:
                    return True
            return False
                
        while not is_prime(n):
            n += 1
        
        return n

    def _resize(self, number: int) -> int:
        self._capacity = self._next_prime(number)

    def __getitem__(self, key: KT) -> VT:
        bucket = self._buckets[self._get_bucket_number(key, len(self._buckets))]
        for (k, v) in bucket:
            print(k, v)
            if k == key:
                return v

        raise KeyError("nfu4orijwgkjhertuoih")

    def __setitem__(self, key: KT, value: VT) -> None:
        if self._count / len(self._buckets) >= self._load_factor:
            self._resize(self._capacity)
        # Prime:
        # Double Current
        bucket = self._buckets[self._get_bucket_number(key, len(self._buckets))]
        if bucket.empty == True:
            bucket.append((key, value))
            self._count += 1
        else:
            bucket.prepend((key, value))
            self._count = (self._count + 1 % self._capacity)


    def keys(self) -> Iterator[KT]:
        for key in self:
            yield key
    
    def values(self) -> Iterator[VT]:
        for (key, value) in self:
            yield key[value]


    def items(self) -> Iterator[Tuple[KT, VT]]:
        raise NotImplementedError("HashMap.items() is not implemented yet.")
            
    def __delitem__(self, key: KT) -> None:
        bucket = self._buckets[self._get_bucket_number(key, len(self._buckets))]
        if bucket.empty:
            raise KeyError("Item not in hashmap.")
        else:
            bucket.pop_front()
            
    
    def __contains__(self, key: KT) -> bool:
        # 1. Get Bucket Index
        bucket_index: int = self._get_bucket_number(key, len(self._buckets))

        # 2. Get Bucket Chain
        bucket_chain: LinkedList = self._buckets[bucket_index]

        # 3. Search for key if it exists
        for (k, v) in bucket_chain:
            if k == key:
                return True # FOUND!!
        
        return False
        
    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        for bucket in self._buckets:
            for (k, v) in bucket:
                yield k
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("HashMap.__eq__() is not implemented yet.")

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)