
class Prompt:
    @staticmethod
    def generate_prompt(question, context):
        prompt = f"""
        You are an intelligent academic assistant.

        Answer the question using ONLY the provided context.

        If the answer cannot be found in the context, reply:
        "I don't know based on the provided document."

        -------------------------
        Context:
        {context}
        -------------------------

        Question:
        {question}

        Answer:
    """
        return prompt