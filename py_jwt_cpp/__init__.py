from typing import Dict
from .jwt_cpp import encode_cpp

def encode(data: Dict[str, str], private_key: str):
    return encode_cpp(data, private_key)
