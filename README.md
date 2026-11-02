# AI Engineer Internship – Week 1

## Project Overview
This repository contains my Week 1 AI Engineer Internship tasks, including Python fundamentals, automated testing, and a Gemini-powered command-line AI assistant.

## Completed Tasks
- Set up Python, VS Code, Git, and a virtual environment.
- Created 10 Python practice exercises.
- Wrote automated tests using pytest.
- Successfully passed all 16 tests.
- Built a command-line AI assistant using the Gemini Developer API.
- Configured environment variables to protect the API key.
- Uploaded the project to GitHub.

## Project Structure

```text
AI-Engineer-Internship/
│
├── exercises/
│   ├── exercise_01.py
│   ├── exercise_02.py
│   ├── exercise_03.py
│   ├── exercise_04.py
│   ├── exercise_05.py
│   ├── exercise_06.py
│   ├── exercise_07.py
│   ├── exercise_08.py
│   ├── exercise_09.py
│   ├── exercise_10.py
│   ├── test_exercise_01.py
│   ├── test_exercise_02.py
│   └── test_exercises_03_to_10.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/musakhani8521-commits/AI-Engineer-Internship.git
cd AI-Engineer-Internship
```

Create and activate a virtual environment on Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## API Configuration

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

Never upload your `.env` file or share your API key.

## Run the AI Assistant

```bash
python main.py
```

## Run Tests

```bash
python -m pytest -v
```

**Latest test result:** 16 passed.

## Important Note

The current application uses the Gemini Developer API. Integration with Google Cloud Vertex AI remains pending access to the internship Google Cloud project.

## Author
Musa Khan