# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - The UI looked good. I noticed that on the side bar it specifies the Range: 1 to 100, but if it was on the main central navigation bar, it would be easier to not guess what the min and max of the guesses would be.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - The score might be calculated incorrectly. I am unable to understand how the score is currently being calculated.
  - The Go Lower and Go Higher code was incorrect, and/or the secret number was changing. I have to debug to figure out the issue.
  - New Game button, creates a new secret number, but it doesn't restart the game.
  - Show hint when checked and then unchecked and checked again doesn't show the hint.
  - If a number is over or under the range of 1-100, return an out of bounds message.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used Copilot.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    - One example where AI gave a correct suggestion was when I asked Copilot about the incorrect “Go Higher” and “Go Lower” behavior. I intentionally gave a vague prompt to see if it could identify the issue on its own. Copilot correctly pointed out that in the check_guess function, the messages were reversed: when the guess is too high, it should say “Go LOWER”, not “Go HIGHER,” and vice versa. I verified this by testing multiple guesses above and below the secret number, and the hints then behaved correctly.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - One example where AI gave a misleading suggestion was when I asked it about the Show Hint checkbox bug. Copilot suggested changing a single line of code and said the issue was fixed. However, when I tested the app, the problem still occurred. I then reprompted Copilot and explained the exact steps that caused the bug. After that, it correctly identified that the hint message was only generated when the submit button was pressed. The final fix involved storing the last hint message so it could be displayed again whenever the checkbox was toggled.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - To determine whether a bug was truly fixed, I repeatedly tested the game with different inputs and tried to intentionally break the app. I tested edge cases such as guesses outside the allowed range and repeated interactions with buttons and checkboxes. If the issue no longer occurred across multiple tests, I considered the bug resolved.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - One test I ran manually was repeatedly toggling the Show Hint checkbox after making a guess. Previously, the hint would disappear after unchecking and rechecking the box. After implementing the fix that stores the last hint message, I confirmed that the hint consistently reappeared whenever the checkbox was enabled again.
- Did AI help you design or understand any tests? How?
  - The AI helped me understand the score logic. At first, I thought the score calculation was a bug because it looked inconsistent. However, Copilot explained that the scoring system rewards correct directional guesses on even attempts but penalizes incorrect guesses or certain odd attempts. Once I understood the proper logic, I realized the score calculation was working as designed and did not need debugging.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - The secret number kept changing in the original app because Streamlit reruns the entire script whenever a user interaction occurs in the app. Since the random number generation was placed in the main script, a new secret number was generated every time the app reran.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - I would explain Streamlit reruns to a friend as the app executing the entire script from top to bottom again every time something happens in the UI. Because of this behavior, variables reset unless they are stored in session state, which allows values to persist between reruns.
- What change did you make that finally gave the game a stable secret number?
  - To fix the issue, I stored the secret number in Streamlit session state so it is generated only once when the game starts and remains unchanged during gameplay. The value only resets when the user presses the New Game button.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - One habit I want to reuse in future projects is asking AI to generate test cases for my fixes. Copilot was very thorough in suggesting ways to test the bugs I fixed and helped me think about edge cases that I might not have considered on my own.
- What is one thing you would do differently next time you work with AI on a coding task?
  - One thing I would do differently next time when working with AI is to describe the bug more clearly. Since AI can only see the code and not the actual behavior of the app, explaining the exact steps I took to reproduce the issue helps guide the AI toward a better solution.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project also changed how I think about AI-generated code. I usually relied on ChatGPT for syntax help or debugging small issues, but using Copilot integrated directly in the IDE was very helpful because it could see all of my project files at once. It provided useful explanations for the changes it suggested, which helped me understand the fixes rather than just copying code.
