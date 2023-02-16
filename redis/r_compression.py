import bz2

blob = "i have a lot to talk about" * 10000

len(blob.encode("utf-8"))

# Set the compressed string as value

r.set("msg:500", bz2.compress(blob.encode("utf-8")))

r.get("msg:500")

# b'BZh91AY&SY\xdaM\x1eu\x01\x11o\x91\x80@\x002l\x87\'  # ... [truncated]

len(r.get("msg:500"))

# 122

260_000 / 122  # Magnitude of savings

# 2131.1475409836066


# Get and decompress the value, then confirm it's equal to the original

rblob = bz2.decompress(r.get("msg:500")).decode("utf-8")

rblob == blob
