# HW 2 - Game AI

**Note:** Run this using Python 3.6/3.7.

## Introduction: Konane

Also known as Hawaiian Checkers, [Konane](https://en.wikipedia.org/wiki/Konane) is a strategy game played between two
players. Players alternate taking turns, capturing their opponent's pieces by jumping their own pieces over them (if 
you're familiar with checkers, there is a strong structural analogy to be made here, except the jumping is not diagonal but orthogonal, and while multiple jumps are allowed in a turn, all jumps have to occur in the same direction). The first player to be unable to capture any of their opponent's pieces loses.

The full rules can be read *[here](https://en.wikipedia.org/wiki/Konane#Rules_and_gameplay)* or
*[here](http://www.konanebrothers.com/How-to-Play.html)*, and *[here's](https://www.youtube.com/watch?v=09AAT29uaGE)* a nice video explaining the rules simply as well.


## Play the game

Run the following from your terminal:
```bash
python main.py $P1 $P2
```

By default, `main.py` will setup a human player versus a random player on a board that is 10x10. During **Human** mode, move the cursor with the ARROW keys and select the tile with SPACE. When it is a computer's turn, advance the game with the SPACE key. To see the game board in your terminal, you need a minimum terminal size of (rows + 2) x (columns + 2) to see the whole board. To exit the game, kill the process in your terminal (e.g., with CTRL-c).

You can change the game settings by passing in values to `python main.py`. You need to pass in _exactly_ two arguments. Valid arguments are as follows:

* H (Human)—manually select the tile to move and to where you will move it. Legal moves will be executed.
* D (Deterministic)—the agent will select the first move that it finds (the leftmost option in the tree) during its 
traversal.
* R (Random)—the agent will pick a random move.
* M (Minimax)—the agent will pick a move using the Minimax algorithm. You will be prompted for a maximum search depth.
* A (Alpha-Beta pruning)—the agent will pick a move using A-B pruning. You will be prompted for a maximum search depth.

Passing in an invalid number or type of arguments will result in the system defaulting to a human vs. a random player.


## Part 1: Minimax

Minimax is an algorithm for determing the best move in an adverserial game. It seeks to minimize the maximum loss posed by the opponent’s strategy. Minimax is typically employed in competitive, discrete-, and finite-space games with abstracted time and perfect information.

Implementation of `MinimaxPlayer` is in `player.py`. The maximum depth is provided to the constructor of the `MinimaxPlayer` and defines the maximum number of plies that the player will simulate when choosing a move. The evaluation function defines a score for a terminal node in the search. The function `h1` defined in the parent class `Player` is the evaluation function.


## Part 2: Alpha-Beta Pruning

You may notice that Minimax starts to get terribly slow when you set your maximum search depth to values above, say, 4. This makes perfect sense when you think about the fact that the total number of nodes in your game tree is the branching factor to the power of the search depth. For comparatively "bushy" games (e.g., _chess_, _Go_, etc.) the branching factor is prohibitively large, which is why agents that play these games use cleverer algorithms to choose what move to take next.

One such cleverer algorithm (although still not clever enough to do well at games like _Go_) is a modification of
Minimax known as _Alpha-Beta Pruning_. They are, at their core, the _same algorithm_. The distinction is that A-B Pruning _ignores_ subtrees that are provably worse than any that it has considered so far. This drastically reduces the runtime of the algorithm.\* Since A-B Pruning is a variant of Minimax, you aren't really writing a new algorithm; rather, you're taking your implementation of Minimax and making it a little smarter.

\* Strictly speaking, it doesn't change the upper bound on the algorithm's runtime, since in the worst-case one must
still search the entire tree. In practice, however, the performance difference is very noticeable.


### Testing

You can find those tests in `test.py`, and you can run them with:

```bash
python test.py
```


## Notes

On the codebase:

* `player.py`—this is the file you'll be editing. Note that `MinimaxPlayer` and `AlphaBetaPlayer` are both diked out and replaced with a determinstic player instead.
* `main.py`—to play the game (in Human mode) or to watch your agents duke it out, run `python main.py`. Use the arrow 
keys and the spacebar to select your actions.
* `test.py`—run tests with `python test.py`.
* `game_manager.py`—holds the board representation and handles turn-taking.
* `game_rules.py`—code determining available moves, their legality, etc.
* You can change the type of player, the board size, etc. in `main.py`
