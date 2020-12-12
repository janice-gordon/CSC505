# -*- coding: utf-8 -*-
###########################################################
# CSC505 Module 1 - Option 1
# Python Script - Fun with Ascii Art
# Janice Gordon
# Ascii art source: https://asciiart.website/index.php
###########################################################

dragon_art = """
             ______________
       ,===:'.,            `-._
            `:.`---.__         `-._
              `:.     `--.         `.
                \.        `.         `.
        (,,(,    \.         `.   ____,-`.,
     (,'     `/   \.   ,--.___`.'
 ,  ,'  ,--.  `,   \.;'         `
  `{D, {    \  :    \;
    V,,'    /  /    //
    j;;    /  ,' ,-//.    ,---.      ,
    \;'   /  ,' /  _  \  /  _  \   ,'/
          \   `'  / \  `'  / \  `.' /
           `.___,'   `.__,'   `.__,'  John VanderZwaag


"""

scary_art = """

                              ''~``
                             ( o o )
+-----------------------.oooO--(_)--Oooo.---+
|                                           |
| They scare me too!      .oooO             |
|                         (   )   Oooo.     |
+--------------------------\ (----(   )-----+
                            \_)    ) /
                                  (_/


"""

dragons = input("Do you like dragons? \nEnter yes or no: ")

if dragons == 'yes':
    print("\nI like dragons too!\n" + dragon_art)
else:
    print(scary_art)
