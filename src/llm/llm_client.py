import ollama

from utils.config import LLM_MODEL


class LLMClient:
    """
    Utility class for interacting with a local Ollama model.
    """

    @staticmethod
    def generate_response(prompt: str) -> str:
        """
        Send a prompt to the Ollama model and return the response.

        Args:
            prompt (str): The full prompt containing context and question.

        Returns:
            str: Generated answer from the model.
        """

        try:
            response = ollama.chat(
                model=LLM_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response["message"]["content"].strip()

        except Exception as e:
            return f"Error generating response: {e}"