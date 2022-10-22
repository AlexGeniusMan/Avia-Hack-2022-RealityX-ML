from typing import Iterable


class Encoder():
    def __init__(self, values: Iterable):
        encoder = {}
        decoder = {}
        for index, val in enumerate(values):
            encoder[val] = index + 1
            decoder[index + 1] = val
        self.encoder = encoder
        self.decoder = decoder
        self.size = len(values)

    def encode(self, vals: list) -> list:
        encoded = []
        for val in vals:
            encoded.append(self.encoder.get(val, 0))
        return encoded

    def encode_single(self, val) -> int:
        return self.encoder.get(val, 0)

    def decode(self, vals: list) -> list:
        decoded = []
        for val in vals:
            decoded.append(self.decoder.get(val, 0))
        return decoded

    def decode_single(self, val: int):
        return self.decoder.get(val, 0)
