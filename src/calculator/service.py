import asyncio
import os
from typing import List


class CodeCalculator:
    source: str
    paths: List[str]

    def __init__(self, source: str):
        self.source = source
        self.paths = []

    async def count(self) -> int:
        self.generate_path_map()

        result = await self.calculate()

        return result

    def generate_path_map(self):
        directory_items = (
            os.path.join(self.source, x)
            for x in os.listdir(self.source)
            if not x.startswith('.')
        )

        for item in directory_items:
            if os.path.isfile(item):
                self.paths.append(item)
                continue

            for root, subdirectories, files in os.walk(item):
                self.paths.extend(
                    [
                        os.path.join(root, x)
                        for x in files
                        if not x.startswith('.')
                    ]
                )

    async def calculate(self) -> int:
        count = 0

        for file_path in self.paths:
            await asyncio.sleep(0)

            with open(file_path, 'rt') as file:
                try:
                    count += len(file.readlines())
                except UnicodeDecodeError:
                    continue

        return count
