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

## Prompt 3

> Perform a brief security review of this calculator. Check for eval/exec, exposed secrets, backend input validation, and Flask debug settings. Report what you find and any necessary fixes. Keep the review within this small assessment’s scope.

### Full user-visible response

Security review completed.

- **`eval` / `exec`:** No use found. Operations use a fixed allowlist of four functions.
- **Secrets:** No API keys, tokens, passwords, private keys, or other credentials found in application files.
- **Input validation:** Appropriate for this assessment. The backend:
  - Requires a JSON object
  - Rejects missing, invalid, boolean, infinite, and `NaN` values
  - Allows only the four supported operations
  - Rejects division by zero
  - Returns clear HTTP 400 errors without exposing exception details
- **Flask debug mode:** [app.py](C:/Users/navid/Desktop/Projects/nucleus-calculator/app.py:47) contains `app.run(debug=True)`. This is acceptable only for local development on the default loopback address. Flask’s interactive debugger must never be exposed publicly.

Necessary fix before deployment:

```python
app.run(debug=False)
```

Alternatively, omit the argument and enable debugging only through a local environment setting when needed.

No other security changes appear necessary within this small assessment’s scope. I added the exact review prompt and a labeled output summary to [AI_PROMPTS.md](C:/Users/navid/Desktop/Projects/nucleus-calculator/AI_PROMPTS.md). That log update is currently local and uncommitted; application code was not changed.

## Prompt 4

> Change app.run(debug=True) to app.run(debug=False). Run the tests again.
>
> Include this security-review prompt and the full user-visible response in AI_PROMPTS.md, not just a summary.
>
> Commit and push the code and AI log changes to the existing repository.

### Output summary

Changed the direct Flask development entry point to run with debug mode disabled, reran the complete automated test suite, updated the prompt log with the prior security-review prompt and full response, and committed and pushed the requested changes. The final assistant response reports the actual test and push results.
