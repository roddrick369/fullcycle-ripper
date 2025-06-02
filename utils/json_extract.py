import base64
import gzip

def decompress(compressed_binary: bytes) -> str:
    return gzip.decompress(compressed_binary).decode('unicode-escape') # type: ignore

def decode(encoded_string: str) -> str: # type: ignore
    decoded_str = base64.b64decode(encoded_string)
    return decompress(decoded_str)
