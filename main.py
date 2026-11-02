
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: API key not found in .env file.")
    raise SystemExit(1)

# Configure Gemini: only one attempt, no repeated retries
http_options = types.HttpOptions(
    retry_options=types.HttpRetryOptions(attempts=1)
)

client = genai.Client(
    api_key=api_key,
    http_options=http_options
)


def ask_gemini(question):
    try:
        print("\nGemini is responding...")

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=question,
            config=types.GenerateContentConfig(
                max_output_tokens=256
            )
        )

        if response.text:
            print("\nGemini:", response.text)
        else:
            print("\nNo response received.")

    except Exception as error:
        print("\nGemini request failed.")
        print("Error:", type(error).__name__)
        print("Details:", error)
        print("\nPlease try again later or check your API access.")

        
def main():
    print("\n==============================")
    print("       AI ASSISTANT")
    print("==============================")
    print("Model: Gemini 3.5 Flash-Lite")
    print("Type 'exit' to close.")

    try:
        while True:
            question = input("\nYou: ").strip()

            if question.lower() == "exit":
                print("Goodbye!")
                break

            if not question:
                print("Please enter a question.")
                continue

            ask_gemini(question)

    except KeyboardInterrupt:
        print("\nApplication stopped.")

    finally:
        client.close()


if __name__ == "__main__":
    main()
