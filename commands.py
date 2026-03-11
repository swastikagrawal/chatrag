from config import MODELS
from pdf_handler import get_pdf_list, load_pdf, load_all_pdfs
from vector_store import build_index


def handle_pdf():
    pdf_files = get_pdf_list()

    if not pdf_files:
        print("System: No PDFs found. Please add a PDF to the /pdf folder and type /pdf to continue.")
        return None, False

    print("System: Select a PDF:")
    count = 1
    for file in pdf_files:
        print(f"  {count}. {file}")
        count += 1
    print("  all - Load all PDFs")
    print("System: If your PDF is not listed, add it to the /pdf folder and type /pdf again.")

    choice = input("You: ").strip().lower()

    if choice == "all":
        print("System: ⚠️  Loading all PDFs, this may take a moment.")
        chunks, sources = load_all_pdfs(pdf_files)
        build_index(chunks, sources)
        print(f"System: Loaded {len(pdf_files)} PDFs successfully.")
        return pdf_files, True

    elif choice.isdigit():
        choice_num = int(choice)
        if choice_num < 1 or choice_num > len(pdf_files):
            print("System: Invalid choice. Please try again.")
            return None, False
        selected = pdf_files[choice_num - 1]
        print(f"System: Loading {selected}, please wait...")
        chunks = load_pdf(selected)
        build_index(chunks)
        print(f"System: {selected} loaded successfully.")
        return selected, False

    else:
        print("System: Invalid choice. Please try again.")
        return None, False


def handle_model(current_model):
    print("System: Select a model:")
    count = 1
    for model in MODELS:
        print(f"  {count}. {model['provider']} - {model['description']}")
        count += 1

    choice = input("You: ").strip()

    if choice.isdigit():
        choice_num = int(choice)
        if choice_num < 1 or choice_num > len(MODELS):
            print("System: Invalid choice. Keeping current model.")
            return current_model
        selected = MODELS[choice_num - 1]
        print(f"System: Model switched to {selected['provider']}.")
        return selected["name"]
    else:
        print("System: Invalid choice. Keeping current model.")
        return current_model


def handle_help():
    print("System: Available commands:")
    print("  /pdf   - Switch or add a PDF")
    print("  /model - Switch the model")
    print("  /help  - Show this help message")
    print("  /exit  - Quit the program")


def handle_exit():
    print("System: Goodbye!")
    quit()