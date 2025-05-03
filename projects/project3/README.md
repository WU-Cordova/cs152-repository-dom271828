1. Structure Choices:
    A. LinkedList for Customer Order. This list of OrderItems (with a __str__ method) reliably displays the name and list of drinks when iterated over. 

    B. Array for Menu, hardcoded array is efficient for pulling from when taking orders.

    C. LinkedList for Confirmation. This wasn't a big one, I just needed to iterate and display OrderItems when customer was done ordering. 

    D. CircularQueue for Open Orders Queue. This was in the name, but the utility is great with reliably enqueuing/dequeuing recent orders. Went with the Array-Based because it uses a simpler data structure.

    E. LinkedList for Completed Orders. Allows for reliable iteration through as many Customer Orders as needed.

2. How to Run   
    The program comes with a hardcoded menu of five drinks, which are put into a BistroSystem class. I then trigger the "run" command which prompts the main menu, and the rest is done using user input. Make your way through the program, adding orders and marking as complete, and when you're done, press 6 to close it. 

3. Program Screenshots
    Images are in the repository. The code runs on my end, so I'm sure you won't have trouble, but look at those for reference just in case. 

4. Limitations
    I feel like the main limitations are accounting for anomalies in user input (i.e. I used an int command at some point to denote a number, and that can pull an error when a user enters a letter in place of a number) which can stop the program prematurely. Additionally, referencing through multiple classes is probably not the most efficient thing, and makes my code confusing for sure.

    OH, and the ordering multiple drinks isn't implemented exactly like it is on the canvas page. There's a limit for drinks someone can order which the user chooses, but I just keep asking for input until the user wants to stop ordering drinks. 

5. Anything else:
    This is already late as is, but I'd say a coupon system, a separate food menu/class, and some type of setting to auto-mark orders as complete were in the running to add. Actually, I think I'll add the last one right now, it's easy enough, but the others would definitely take a little time to ponder on. 

Thank you for a great semester! It was great having you as my teacher. You were always very helpful and also extremely accomodating with due dates and such. Excited to have you again next semester, have an amazing summer!