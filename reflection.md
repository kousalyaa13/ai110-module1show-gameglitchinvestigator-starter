# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - The UI looked good. I noticed that on the side bar it specifies the Range: 1 to 100, but if it was on the main central navigation bar, it would be easier to not guess what the min and max of the guesses would be.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - The score was calculated incorrectly.
  - The Go Lower and Go Higher code was incorrect, and/or the secret number was changing. I have to debug to figure out the issue.
  - New Game button, creates a new secret number, but it doesn't restart the game.
  - Show hint when checked and then unchecked and checked again doesn't show the hint.
  - If a number is over or under the range of 1-100, return an out of bounds message.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    - I told Copilot that the Go Lower and Go Higher code is incorrect. I tried to be vague to see if it is able to identify the issue. And yes, it was able to. It said that in the check_guess function, the "Go Higher" and "Go Lower" messages are reversed. When the guess is too high, it should say "Go LOWER", not "Go HIGHER", and vice versa.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - I told Copilot about the show hint when checked and then unchecked and checked again doesn't show the hint bug. It fixed one line of code and told me it fixed it. However, upon testing, the code doesn't work. The change it suggested didn't work. So I reprompted with the exact steps I took to encounter the error. Then it was able to identify that the hint message is only generated and displayed when the submit button is pressed. It them implemented a way to store the last message and display it again when the checkbox is checked.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I tested each of the bugs using different inputs and parameters. I tried to purposefully break the app to see if any other bugs come to surface. When the bug I was working on isn't occurring again, I know it is fixed.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
