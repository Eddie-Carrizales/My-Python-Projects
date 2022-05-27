# Program name: Treasure Island Mini Game
# Author:      Eddie F. Carrizales
# Date:        05/27/2022
# Description: This program is a mini game that asks questions and is guided through conditionals by the players answers.

print("""
                 _
                ;`',
                `,  `,
                 ',   ;   ,,-""==..,
                  \    ','          ;
          ,-""'-., ;    '    __.-="-.;
        ," ,,_    "'      _."
       ;,'   ''-,          "=--,_
              ,-''    _  _       `,
             /   ,.-+(_)(_)---.,   ;
            ,'  /   ; (_)       `\ ,
            ; ,/    ;._.;         ;
            !,'     ;   ;
            V'      ;   ;
                    ;._.;
                    ;   ;
                    ;   ;        ~
     ~              ;._.;
               ~    ;   ;
                   .'   `.                ~
             __,.--;.___.;--.,___
       _,,-""      ;     ;       ""-,,_
   .--'            ;     ;             ``-.
  ",              ;       `               ,"        ~
    "-_                                _-"
~       ``----..,_          __,,.....-.
                  ```'''''''''                 ~
                              ~
             ~

""")

print("Welcome to the Treasure Island")
print("You have arrived to this island looking for treasure!")
print(
    "Along your search you will encounter many obstacles, but if you take the right path and are careful you may find its treasure.")

answer = str(input("Where do you want to start? Type \"Jungle\" or \"Beach\" \n").lower())

if answer == "jungle":
    print("""
    
 |   [  | v':    :              |        |_,;c    
 | ]    |/; |,   |              |   [  ( __,/     
 |    ,-'/  ;\ ,<  _',\.-._,;   |      ] |    n   
 |   -' /   _;';    '=_'-' ,)  ,\        |   ,;   
 |  ]  / \,'__/--,_,-- 'mm'J -"_  ]       '-,+_   
 |    /    / "''-.,;"---''--'"" \      ]   __  "-'
;' [      / :    : _c           /         /  ",_,'
|      [ | v|  , '/             c c    \ |        
\    ]   |  \ /| :        __,-,v;|]   . \|        
  [      /"--'/  |      (7_   c@  )    )/|        
\     ]    ,-"'<':       '--,    (    /^ |        
| ]       / :   '|           \ |  )      |        
| |   /  |  |    ;,-;,        \ ,)(     ]|        
|  \^ |  |  :  |\ ,'           \ / \ [   |        
|  ?  /  \_ |  /|:              | , \    |        
|  | ('.   "--' |:,    ;        :\  ,\  [|        
|  ;\~)   _     \_) ',_|   ,    | ),  \_ :        
|   |/ [ /""-,_   '-'(    /.'   | \   |  '-_      
| [      |  |  "---,__"'=';=,_  |  \ /|\    '"-,__
|     ]  |  :    |    ""'^.\    |   | |    \      
|  [    ]|  |    :              | ]  \ \   /  
    """)
    answer = str(input(
        "You are walking through the jungle when you hear a loud noise. What do you do? Type \"Run\" or \"Listen\" \n").lower())
    if answer == "run":
        print("""
                        ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/      ,/;,
               ,-' /'  _    / _/
               ` /     _/  ` /
                 |     /,  `_/
                 |     \'
     /  _         /`       /
   /' /_``--.__/  `,. /  
  |_/`  `-._     `/  `   `.
            `-.__/'     `   |
                          `  \
                            ` \
                              ___
                               ___)
        """)
        answer = str(input(
            "You keep running through the jungle and you reach a crossroad. On the left a dirt trail. On the right a river. Where do you go? Type \"Left\" or \"Right\" \n").lower())
        if answer == "left":
            print("""
                    /   \              /'\       _                              
\_..           /'.,/     \_         .,'   \     / \_                            
    \         /            \      _/       \_  /    \     _                     
     \__,.   /              \    /           \/.,   _|  _/ \                    
          \_/                \  /',.,''\      \_ \_/  \/    \                   
                           _  \/   /    ',../',.\    _/      \                  
             /           _/m\  \  /    |         \  /.,/'\   _\                 
           _/           /MMmm\  \_     |          \/      \_/  \                
          /      \     |MMMMmm|   \__   \          \_       \   \_              
                  \   /MMMMMMm|      \   \           \       \    \             
                   \  |MMMMMMmm\      \___            \_      \_   \            
                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          
                    /'.,___________...,,'   \            \   \        \         
                   /       \          |      \    |__     \   \_       \        
                 _/        |           \      \_     \     \    \       \_      
                /                               \     \     \_   \        \     
                                                 \     \      \   \__      \    
                                                  \     \_     \     \      \   
                                                   |      \     \     \      \  
                                                    \ms          |            \ 
            """)
            answer = str(input(
                "You take a left and continue through the dirt trail. You notice a cave up ahead, but the dirt trail continues past the cave. Do you go in the cave or continue the trail? Type \"Cave\" or \"Trail\" \n").lower())
            if answer == "cave":
                print("""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
                """)
                print(
                    "As you are entering the cave your flashlight makes something shine bright yellow in the darkness. Its the treasure! ")
                print(
                    "Congratulations! You have found the treasure! You walk back the way you came from and safely make it with your pockets full of gold.")

            else:
                print("""
                         _
                       _( }
                  _  //  ;
                 `.__/`/\\
                   '--'\\  `
                       //
                ~~~~~~~\)~~~~~~~~
                 """)
                print(
                    "You continue through the trail but accidentally walked over quicksand, unfortunately, no one is around to help you. You sink, suffocate, and die. Game Over.")
        else:
            print("""
                     _.---._     .---.
            __...---' .---. `---'-.   `.
  ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
 -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
  ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
     ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
         ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
             ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                     ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~
            """)
            print(
                "You take a right and attempt to cross the river. You almost made it across except a large crocodile wanted a snack. You were the snack, and died. Game Over.")
    else:
        print("""
                            _.--....
                 _....---;:'::' ^__/
               .' `'`___....---=-'`
              /::' (`
              \'   `:.
               `\::.  ';-"":::-._  {}
            _.--'`\:' .'`-.`'`.' `{I}
         .-' `' .;;`\::.   '. _: {-I}`
       .'  .:.  `:: _):::  _;' `{=I}.:|
      /.  ::::`":::` ':'.-'`':. {_I}::/
      |:. ':'  :::::  .':'`:. `'|':|:'
       \:   .:. ''' .:| .:, _:./':.|
        '--.:::...---'\:'.:`':`':./
                       '-::..:::-'
        """)
        print(
            "You stop and listen to the noise when suddenly a cobra lunges itself at your leg and bites you! Everything goes black, you died. Game Over. ")
else:
    print("""
                              +                              
               /         -/          ,                   
               #        .#         -#.                   
               #        #,       -##.                    
               #       ,#       %##                      
               #       -##     /##                       
               #,       ###    ###                       
               ##/      ;##    ###                       
     ,         ####+     ##-   ###            .          
      %        ,#####   ;##-  :###     -#####/           
      :%         ;###   ###  #####    :##+,              
      ,#;         ###::/##########   ,###                
       ##/..,-    ####/,   .-:###;   ###=                
       ,#######:  ##=          .%#+#####                 
        ,#######=++              -#####=                 
             ####;                .##;                   
              ##/  ;###%    ,%##%- ,#                    
               % ,#:-=##=  ,#/::+#= +;=.   %###=         
               -           #.     ,  ###:;#######=       
 =;      +###%#    -####, -+ +###-   #######;   -:=.     
  =#+  :#######    -,##   ;: ,##%.   +#####,             
   -###########      .    /:   .     /#//:               
    .#####:/##%           //         /                   
              %           /+         /-                  
              #           :#         ##/  ,-             
            /##.          +#         ########+           
          =####/         %##        /#########+          
         ,######,                  .; +##%-  +#=         
         ########     :#+#%###/    #          =#.        
       ,%###   -##      .;#/,     ###           /.       
 .:+######%    .###.     #/%:   -####                    
      =//-    =#####+.    =,  ,#; %###=                  
              #########:   ./###   #####:                
              #####% ###########    +####=               
              ####   #####%  ###       /#%               
              ###/   #####   ###        ##               
             .###.   ####   /###,       ,#               
            -###=    ####    %##+        #               
          -###%,     ####.    %##        --              
         ;:.         ;###=     ##         .              
                     .###=     +#               
                     =###      =/                        
                     ###       ,.                        
                    ;#:                                  
                    #.                                   
                   -      
    """)
    print("You forgot to bring water, got dehydrated, and died. Game Over.")
