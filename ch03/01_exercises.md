# Exercises

1. Suppose I show you a call stack like this.
    What information can you give me, just based on this call stack? 

    <table>
        <tr>
            <td colspan="2" style="text-align:center;">Greet2</td>
        </tr>
        <tr>
            <td>name:</td>
            <td>Maggie</td>
        </tr>
        <tr>
            <td colspan="2" style="text-align:center;">Greet</td>
        </tr>
        <tr>
            <td>name:</td>
            <td>Maggie</td>
        </tr>
    </table>

    That means that you called the function "Greet" in the "main" function with
    "Maggie" as name argument and inside this function you executed "Greet2" with
    also "Maggie" as an argument.


2. Suppose you accidentally write a recursive function that runs
forever. As you saw, your computer allocates memory on the
stack for each function call. What happens to the stack when your
recursive function runs forever?

    We got a Stack Overflow error, because the program only has a limited space
    assigned to function calls.