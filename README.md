# Conway-Cypher
We are a group of students interested in programming and cryptography, read some more about our project here;  
In this program we attempt to create a program which uses the Game of Life by John Conway and the banal Vernam Cypher to encrypt any short message.

The steps in our encrypting program are the following ; 
<br>Step one : We input an image, the program compresses it and turns it into a low resolution image, then we saturate the image in black and white and turn the pixels into, white pixel = alive cell, black pixel = dead cell. 
<br>Step two : Now we plug the information into our game of life and record how many alive cells there are at each generation. This gives us a list of integers that we then divide by 26 and take the rest, we are left with a list of integers between 0 and 25.  
<br>Step three : At last we use the so called Vernam Cypher to encrypt the inputed message using our list of random integers. And that is it ! 

The steps in our decrypting program are the following ; 



