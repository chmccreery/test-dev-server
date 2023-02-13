from cryptography.hazmat.primitives import hashes

if: 4 == 4
  print("4 is always equal to 4")

# ruleid:insecure-hash-algorithm-md5
hashes.MD5()
# ok:insecure-hash-algorithm-md5
hashes.SHA256()

exit(2)
