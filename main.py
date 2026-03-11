from commands import handle_pdf, handle_model, handle_help, handle_exit
from vector_store import search
from api_handler import get_answer


def main():
    print("System: Welcome to ChatRAG!")
    print("System: Only add open and unprotected PDFs to the /pdf folder.")

    current_pdf, is_super_mode = handle_pdf()
    while current_pdf is None:
        input("Press Enter to try again...")
        current_pdf, is_super_mode = handle_pdf()

    current_model = handle_model(None)
    while current_model is None:
        current_model = handle_model(None)

    print("System: ChatRAG is ready! Type /help to see available commands.")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.startswith("/"):
            if user_input == "/pdf":
                current_pdf, is_super_mode = handle_pdf()
            elif user_input == "/model":
                current_model = handle_model(current_model)
            elif user_input == "/help":
                handle_help()
            elif user_input == "/exit":
                handle_exit()
            else:
                print("System: Invalid command. Type /help to see available commands.")
            continue

        chunks = search(user_input)

        if not chunks:
            print("ChatRAG: I cannot find this information in the provided document.")
            continue

        result = get_answer(user_input, chunks, current_model)

        if result == "RATE_LIMIT":
            print("System: Rate limit reached. Please switch model with /model.")
        elif result == "MODEL_UNAVAILABLE":
            print("System: Model unavailable. Please switch model with /model.")
        elif result == "ERROR":
            print("System: Something went wrong. Please try again.")
        else:
            if is_super_mode:
                sources = []
                for chunk in chunks:
                    if "source" in chunk and chunk["source"] not in sources:
                        sources.append(chunk["source"])
                source_str = ", ".join(["'" + s + "'" for s in sources])
                print("ChatRAG: " + result + " ~ sourced from " + source_str)
            else:
                print("ChatRAG: " + result)


main()