import json
import os
from utils.config import PROCESSED_FOLDER
from utils.logger import Logger


class ChunkSaver:

    @staticmethod
    def save_chunks(chunks, file_name):
        """
        Save chunks to a JSON file.
        """

        os.makedirs(PROCESSED_FOLDER, exist_ok=True)

        chunk_data = [
            {
                "chunk_id": i,
                "text": chunk
            }
            for i, chunk in enumerate(chunks)
        ]

        output_path = f"{PROCESSED_FOLDER}/{file_name}.json"

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(
                chunk_data,
                file,
                indent=4,
                ensure_ascii=False
            )

        Logger.info(f"Chunks saved to {output_path}")