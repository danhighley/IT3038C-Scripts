* Lab 7

==========

***For Lab 7, I chose to do a Python script using the plugin called NumPy

==========

***What is NumPy

NumPy is the primary tool for scientific computing in Python. It combines the flexibility and simplicity of Python with the speed of languages like C and Fortran. NumPy brings the computational power of these languages to Python, a language much easier to learn and use. With this power comes simplicity: a solution in NumPy is often clear and elegant. NumPy is mainly used for its support for N-dimensional arrays. These multi-dimensional arrays are 50 times more robust compared to Python lists, making NumPy a favorite for data scientists.

==========

In the scipt for Lab 7, I focused on a few simple 2D array functions that NumPy can easily handle. I wrote the script on a Windows 11 system using Windows PowerShell and Windows PoserShell ISE.

==========

**Setup

You have a couple options to run this script:

    - from a Python virtualENV

    - or directly from you local machines github repository

    depending on what your comfortable with.

*VirtualENV setup

Following the Week 7 documentation didn't work for me so I had to do a little research.

    -pip wasn't working from PowerShell

    -and my system didnt have the folders set up to match commands outline in Week 7 docs.

Again, I did this in Windows 11.

Decide where you want you python virtual environment to live.

    I created the folder venv on my C directory

    Move to that directory

    `C:\venv`

    In that directory run the following command

    `python -m venv NumPy`   // the last "NumPy" is folder name and can be anything you want.

    `cd NumPy`   // to move into the environment folder then type:

    `Scripts\activate.ps1`

    You should see (NumPy) in front of your command line like this:

    (NumPy) PS C:\venv\NumPy>

    You know your virtual python environment is working if you do.

    Now you can install the python plug in module NumPy by typing:

    `pip install numpy`

    Now you should be able to copy the script to a .py file and run it.

*Installing Numpy on your local machine with out using VirtualENV

After reading the documentation and learning how wide spread the use of NumPy is, 
I decided to install it on my local Windows 11 system and run the script from my 
local github repository.

The Issue I had was pip command wasn't recognized by PowerShell.

If you encounter this, it is a problem with the PATH in environmental variables.

These are the steps I used to resolve my issue.

    You must declare path variable by following these steps:
    1.	Right click on My Computer or This PC.
    2.	Click on Properties.
    3.	Click on Advanced System Settings.
    4.	In the System Properties window click on the Advanced tab.
    5.	Pm the Advanced tab click on Environmental Variables..
    6.  In the environment variables window click on Path from the list of variable and values that shows up there.
    7.  With Path highlighted click edit. 
    You will find a New button in the pop up.
    8.  Click that and paste the location of the python311 folder (The location you specified while installing python) followed by \Scripts there.
    For example C:\Users\a610580\AppData\Local\Programs\Python\Python311 
    so I type   C:\Users\a610580\AppData\Local\Programs\Python\Python311\Scripts
    9.  Move the newly added path up under the python\launcher.
    10. Click Ok to close all windows and restart your command prompt.
    I repeat - restart your command prompt.
    Everything should now be working fine! 
    Make sure you don't disturb anything else in the path variables list 

After correcting my PATH issue, I was able to

    `pip install numpy`
    
    Allowing me to run the script from the PowerShell command line and develop the script using
    PowerShell ISE.

===========

**The script

The script is called Lab7_NumPy.py and should be in this same folder on github.

NumPy makes working with arrays fairly simple, so in the script I focused on a few simple 
examples to show the ease at which NumPy manipulates an array to extract data.

I start by creating a 2D array using NumPy: 5 columns and 5 rows of random integers.

```array = np.random.randint(100, size = (5, 5))```

 Random 5x5 array  
[[51 76 32 48 78]  
 [23 87 61 99  9]  
 [10 10 62 28 77]  
 [77 92 38 30 29]  
 [85 93 76 19 64]]

The first part of the script shows the use of argmax, argmin, max and min by pulling out minimum, maximum values, the indices of where they are, and calculating the positions.

```print("\nThe highest value of the array is: %s, at indices: %s, or at position: %s of the array." % (array.max(),np.argmax(array),np.argmax(array)+1))```

`The highest value of the array is: 99, at indices: 8, or at position: 9 of the array.

The lowest value of the array is: 9, at indices: 9, or at position: 10 of the array.

The average of the random values contained in the entire array is: 54.16.`

Then I move into demonstrating how NumPy can easily parse out values from individual rows and columns
by asking the user to randomly pick which row or column to have the script parse.
Here I uses some regex to ensure correct user input.

```while True:
    selection = input("please select either [1]row or [2]column: ")
    if not re.match("[1-2]*$", selection):
        print("Error! Please enter a [1] or a [2]")
    else:
        break     ```

 Random 5x5 array
[[24 44  9 47 38]
 [38 80 22 67  1]
 [32 59 93 34 98]
 [12 90 58 60 26]
 [ 4 57 84 36 59]]

`NumPy can even parse the array at the row or column level.
please select either [1]row or [2]column: 1
Please select which row [1-5]: 2

The maximum value found in row 2 is 80.`

Then I demonstrate how NumPy can add arrays together

Original Random array
[[78 28 57 90 31]
 [86  2 60 64 19]
 [25 33 81 50 88]
 [93 91 67 68 50]
 [ 8 21 50 95 72]]

Combined with an array of 2s
[[2 2 2 2 2]
 [2 2 2 2 2]
 [2 2 2 2 2]
 [2 2 2 2 2]
 [2 2 2 2 2]]

      Equals
[[80 30 59 92 33]
 [88  4 62 66 21]
 [27 35 83 52 90]
 [95 93 69 70 52]
 [10 23 52 97 74]]

 These examples are simple and are barely scratching the surface of NumPy's capabilities, but I hope the code shows how easily NumPy manipulates arrays.

===========
