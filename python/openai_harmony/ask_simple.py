"""
Simple Q&A interface - lightweight and fast!
"""

import os
import sys
import subprocess


def main():
    print("=" * 60)
    print("🤖 Q&A Module - Trained on Your PDF Data Only")
    print("=" * 60)
    
    # Check for Ollama
    print("\n⚙️  Checking for Ollama (local AI model)...")
    try:
        response = subprocess.run(
            ["ollama", "--version"],
            capture_output=True,
            timeout=2
        )
        if response.returncode != 0:
            raise Exception("Ollama not found")
        print("✅ Ollama found\n")
    except Exception as e:
        print(f"❌ Ollama not installed or not running")
        print("   Make sure 'ollama serve' is running in another terminal!")
        return
    
    # Check for PDF
    pdf_path = "data/exchange.pdf"
    if not os.path.exists(pdf_path):
        print(f"❌ Error: PDF not found at {pdf_path}")
        sys.exit(1)
    
    # Import and initialize
    print("🔄 Initializing Q&A module...")
    from qa_simple import CustomQAModule
    
    try:
        qa = CustomQAModule(pdf_path)
    except Exception as e:
        if "Connection refused" in str(e) or "Errno 111" in str(e):
            print(f"❌ Cannot connect to Ollama on http://localhost:11434")
            print("   Make sure 'ollama serve' is running in another terminal!")
            return
        raise
    
    # Interactive Q&A
    print("\n" + "=" * 60)
    print("📝 Ask questions about your PDF (type 'quit' to exit)")
    print("=" * 60)
    
    while True:
        question = input("\n❓ Your question: ").strip()
        
        if question.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye!")
            break
        
        if not question:
            continue
        
        print("\n🔍 Searching your data...")
        result = qa.ask(question)
        
        print(f"\n✅ Answer:\n{result['answer']}")
        if result['sources']:
            print(f"\n📄 Source chunks: {result['sources']}")


if __name__ == "__main__":
    main()
