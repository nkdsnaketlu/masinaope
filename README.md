Using [Chat GPT](https://chatgpt.com/share/6aa9b7f9-0cfc-83eb-8170-d957c3184359) I generated a simple Battleships game.

First I asked to come up with simple rules

prompt:
> Come up with basic rules for the game like battleships, but where each players have 3x3 field, one 2 cell ship and two 1 cell ships

Then using those rules I asked him to creato a python code

prompt:
> Create a simple python code for the console version of this game, based on rules that you've come up

## 1st version
The first version was pretty good already, but the problem was inconsistent appearence of both players fields.
e.g first field looks like: 
```
 _ 1 2 3
 1 * S *
 2 S * *
 3 * S S
```
 After one hit on (1.2) it changes to smth like:
```
 _ 1 2 3
 1 * X S
 2 * S *
 3 * * S
```
 As if transferring the contents of the field or sometimes even combinig 2 fields together. Bcs of that one game could last much longer, bcs field(s) was(were) changing.

## 2nd version
 After politely asking GPT to apply some changes to a code, he changed so it is now 2 player game, not human vs machine 
 But it still feels confusing, bcs of the combined fields and titles like "your field" or "enemy field"

 so I asked for some adjustments

 prompt:
 > change the text "your board" and "enemy board" to "player 1 board"/"player 2 board".
> if one player hit other players ship, dont mark that on their field, only on the opposite one.
