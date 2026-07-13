from langchain_text_splitters import RecursiveCharacterTextSplitter

from utils.config import CHUNK_SIZE, CHUNK_OVERLAP


class Chunker:
    """
    Utility class for splitting text into overlapping chunks.
    """

    @staticmethod
    def create_chunks(text: str) -> list[str]:
        """
        Split the given text into overlapping chunks.

        Args:
            text (str): Cleaned document text.

        Returns:
            list[str]: List of text chunks.
        """

        if not text.strip():
            return []

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                " ",
                ""
            ],
        )

        return text_splitter.split_text(text)