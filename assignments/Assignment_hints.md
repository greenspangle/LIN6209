# Hints & Tips for Programming Assignments

**Important**:  Any program you submit for an assignment MUST execute. <br/>You do NOT need to delete the
faulty code, just comment it out so that I can still read it and award you credit for it.

1. To keep things simple, copy the function you are working on into its own python script. Get it working
   there and then, when it's done, copy it back into the assignment script. This avoids the situation where
   a problem with one function cascades through the whole script stopping any of it from
   executing.<br/><br/>
2. If the explanatory text (green in IDLE) and comments (red in IDLE) I included in the assignment script is
   confusing you or causing you a problem then delete it. It does NOT need to included in your
   submission.<br/><br/>
3. DO NOT use print() statements to 'return' the value from your function. Always put the value you want
   your function to return directly into a return statement.
   ``` python
          # NOT this
          print(the_answer)
   
          # NOR this
          return print(the_answer)
   
          # THIS is the correct way
          return the_answer
      
    ```

4. Do use print statements when debugging. If your function is not doing what you want/think it should be
   doing use print() to print some of those internal values to the console so that you can see what's
   actually going on. When you're done, just comment them out.<br/><br/>
5. Read the error messages. They will usually tell you what is wrong.<br/><br/>
6. Use the Python documentation (and other resources) to help you. For example: If you have a string and you
   want to do 'X' to it then check if there is a built-in function that already does
   that (https://docs.python.org/3/library/functions.html) or that there is a string method that does
   it (https://docs.python.org/3/library/stdtypes.html#textseq). <br/><br/>
7. Test that your functions actually work. As well as any tests of your own, test your functions with the
   examples given in the assignment.<br/><br/>
8. Once your function is working and you have run it, use dir() to check your function is in memory and use
   type() to determine the type of the value your function returns.<br/><br/>
9. If you are stuck / confused / drowning-in-confusion or just have a question or are curious about a
   language feature, do come to my office hours or post on the forum.<br/><br/>