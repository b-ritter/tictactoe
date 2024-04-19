# Tic-tac-toe

## Overview
This implementation of tic-tac-toe is a simple, terminal based Python application. I chose this task because the majority of code I write is heavily dependent on libraries. That said, it also sounded like a fun way to go back to basics.

## Instructions
Clone the repository. You'll need a python3 environment to run the script. From the `tictactoe` directory run `python3 main.py`. Instructions are shown in the prompts. To show help, press the `h` key at any prompt.

## Testing
The controller, model and view all have a suite of unit tests. The game component also has some basic tests to verify game play functionality. All are implemented with the Python standard library `unittest` framework. To run tests, enter ```python3 -m unittest```.

## Design
This implementation leverages two design patterns: Model View Controller and a Finite State Machine. I chose to use the [MVC pattern](https://course.ccs.neu.edu/cs5010f18/lecture10.html) based on my experience with Front End development. At the time, Udacity taught front-end web programming by implementing a simple MVC framework from scratch. This lesson was super important in my transition from an "artist who codes" to a software engineer. Using powerful abstractions allows the programmer to do more, with less effort and strain. Likewise, another project called for us to implemnent the arcade game [Frogger](https://en.wikipedia.org/wiki/Frogger) in JavaScript. Here, the Finite State Machine abstraction served a similar purpose. Reasoning through the logic of the game as a series of discrete states allows one to disentagle heaps of ["spaghetti code."](https://en.wikipedia.org/wiki/Spaghetti_code#:~:text=Spaghetti%20code%20is%20a%20pejorative,with%20insufficient%20ability%20or%20experience.)

## Next Steps
The issue with this design is that it could be difficult to scale. Imagining this as a network-based application, with two players accessing the same game over a shared network connection, is difficult. As is, one has to physically share the keyboard with another player. (I tested the game with my son this way.) If I were to implement this as a web-based game, I would look into a framework like [boardgame.io](https://boardgame.io). This framework leverages the Redux library for state management. In Redux, game (or web application or whatever) is represented as a JSON object. That object gets "passed around" from client a to server back to client b. At the same time, you also might want to persist game state to a document based database such as mongodb.
