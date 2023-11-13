# Iyer, Surya [BSD]
# 10:49 AM (32 minutes ago)
# to me
# Hello Viacheslav,
# Hope you are doing well. This is in reference to the initial assessment test  for the role Senior Software Engineer in Test ( JR24081) with UChicago BSD- CTDS.
# Can you please click the ink and work towards taking the initial assessment ? You will be asked to provide their name and email address before beginning the assessment.
# Once you are done completing them, please do let me know via email and or call. Thank you!
# Please find the  link for assessment - https://coderbyte.com/sl-candidate?promo=centerfortranslational-teypq:software-engineer-cb4oq8vtl3
# I would appreciate if you can acknowledge my email. Thank you!

# Q: Q: What is the difference between git merge and git rebase?
# A:Difference between git merge and git rebase is how much of the history is preserved in the merge.
# With git merge you're adding your code to (usually) the main branch, and all the history is preserved.
# With git rebase you usually adding to your local repository changes from other than your changed
# files happened in main branch since you created your branch
# (other people might have merged their code to the repo).

# Q: What are some tools you have used to test software applications?
# A: Selenium WebDriver. Cypress. Postman. Locust. Jmeter.

# Q: How do you find a list of files that have been changed in a particular commit?
# A: In the links on the GitHub.

# Q: Explain the difference between regression testing and retesting.
# A: Regression testing – is running the entire test suite
# (it is opposite to acceptance/smoke testing when you're running just a short
# subset of the most important tests to make sure the application doesn't crash).
# No companies I worked for used the term "retesting", but I would guest it's when
# you're manually reproducing failed test to check if it's the application error,
# or the app is in good shape, and it's the test is out of sync with reality,
# and needs to be adjusted.

# Code challenge:
# Extract the longest word from the string
def StringChallenge(sen):
    words = sen.split()
    largest_word = max(words, key = len)
    return largest_word

print(StringChallenge(input('Enter the string: ')))


