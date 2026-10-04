# AI Prompts

Prompts supplied during this exercise are recorded below.

## Prompt 1

> The repository is now cloned at `C:\Users\navid\Desktop\Projects\nucleus-calculator`. It is empty. Build the Flask calculator here, test arithmetic and error handling, and keep all changes local without pushing to GitHub. Record all my prompts in `AI_PROMPTS.md` for the exercise submission.
>
> Help me build a small calculator web application for a Nucleus Security internship assessment.
>
> Use Python Flask for the backend and plain HTML, CSS and JavaScript for the frontend.
>
> Requirements:
> - Two number inputs.
> - An operation selector: addition, subtraction, multiplication and division.
> - A Calculate button and a visible result.
> - Perform calculations on the backend through POST /api/calculate.
> - Validate inputs on the backend and return clear errors for invalid input and division by zero.
> - Keep the implementation simple, suitable for a roughly 50-minute exercise.
> - Include requirements.txt, a .gitignore and a README with setup and run instructions.
> - Verify basic arithmetic and error handling, and report what you actually tested.
>
> Explain how the frontend communicates with the backend so I can understand the code. Do not publish to GitHub yet.

### Output summary

Created a Flask calculator with a plain HTML, CSS, and JavaScript frontend. Added the `POST /api/calculate` endpoint, backend validation, error responses, automated tests, dependency and ignore files, and setup documentation. Created a local virtual environment and reported that all 13 tests passed. No commit or push was performed in response to this prompt.

## Prompt 2

> Review the changes in nucleus-calculator and confirm that no secrets or unnecessary files are included.
>
> Update AI_PROMPTS.md with the actual prompts and a summary of the outputs from this task. Clearly label summaries; do not invent prompts.
>
> Commit the calculator and push it to my existing GitHub repository:
> https://github.com/golden-horizon/nucleus-calculator
>
> Report whether the push succeeded.

### Output summary

Reviewed the repository for secret-like values and unnecessary generated files. Confirmed that the virtual environment, pytest cache, and Python bytecode are ignored. Updated this prompt log, reran the automated tests, committed the intended project files, and attempted to push the commit to the existing GitHub repository. The final assistant response reports the actual test and push results.
