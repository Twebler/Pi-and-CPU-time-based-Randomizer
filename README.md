# Pi-and-CPU-time-based-Randomizer
Description:
-Small script that returns a pseudo-random number inbetween 0 and 9 based of CPU-time and digits of Pi


explanation about the number 1424 in the code:
-while trying to figure out how to code this thing i realised that maybe some amount of numbers will be more accurate than others for example in the first 100 digits there are:


  0: 8

  1: 8

  2: 12

  3: 12

  4: 10

  5: 8

  6: 9

  7: 8

  8: 12

  9: 13


  those numbers also correspond to the respective percentages this is highly inaccurate since 13% and 8% are very different percentages so i decided to use the first 1500 digits of pi and leave it at that but since pi is irrational i could be unlucky and the dirstribution of numbers in the first 1500 could still be very uneven so i wrote a small script that iterates through every amount of digits inbetween 32 which is the first time all of the numbers have appeaared in pi and 1500 and find the set with the most even distribution of numbers and turns out 1424 is the amount of digits after the decimal point at which the distribution is the most even at least inbetwenn the digits 32 and 1500 in theory the distrobution gets move even the more digits to look at even though it isnt proven that pi is a normal number but the distribution is very even even over insane amounts of digits.
Now in theory the more digits or subsets you look at or different irrational normal numbers maybe not even a irrational number the accuracy might be higher or have a random number gen with only specific numbers like 0.135135135... which would be a random num gen with only 1 3 and 5. also i did this in python a painlfully slow language so in another language like C you might be able to have a random number gen with more than just the first 1424 digits and thus make it much more accurate. Also the rounded percantages for the first 1424 digits are as follows:


  0: 9.55

  1: 11.03

  2: 10.18

  3: 10.04

  4: 9.41

  5: 10.04

  6: 9.48

  7: 9.62

  8: 9.97

  9: 10.67


  as you can see in still see some moderate inaccuracies but its alot more accurate than 13% and 8%.
