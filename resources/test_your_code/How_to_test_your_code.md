# Test Your Code

Untested code is unreliable code. It might work perfectly, but it probably won't.

There are many ways you can test your code:

1. Desk-check the code and assume that it works
2. Run the code in IDLE and do some ad-hoc testing
3. Write a list of tests that cover all the functionality and run them manually
4. Write a list of tests that cover all the functionality and write some code to run them automatically.
   This testing code could be:
    1. None-existant.
    2. Tests output two columns: 'expected outcome' vs 'actual outcome'. Inspect that output manually for
       differences.
    3. A sequence of try-except statements using `assert` statements that onluy output failed tests.
    4. Built on a test framework such as 'pytest'
