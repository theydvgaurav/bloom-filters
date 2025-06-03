# Bloom Filter Implementation in Python

This repository contains a minimal yet functional implementation of a **Bloom Filter**, a space-efficient probabilistic data structure used to test whether an element is a member of a set. It is implemented in pure Python and utilizes cryptographic hash functions (`MD5`, `SHA-1`, and `SHA-256`) for generating hash indices.

---

## Features

- Lightweight and easy-to-understand implementation
- Uses three different hash functions for better distribution
- Demonstrates core Bloom Filter operations: **add** and **search**
- No external dependencies beyond Python’s standard library

---

## How It Works

A Bloom Filter allows for efficient membership checks with a small memory footprint. It supports:

- **Insertions**: Always accurate.
- **Lookups**: May yield **false positives**, but **never false negatives**.

This implementation uses a fixed-size bit array of 10 bits. Three hash functions generate indices between `0` and `9` which are then used to set or check bits.

---

## Usage

### 💻 Example
```python
from bloom_filter import BloomFilter

bf = BloomFilter()
bf.add("Gaurav")

print(bf.search("Abhinav"))  # Likely False
print(bf.search("Gaurav"))   # True
