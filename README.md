# NCAA-Project

Predicting NCAA Men’s Basketball Win Percentage and Close Game Percentage by Time and Points Difference

As a spectator watching a basketball game, I always want to know how close my team is
to winning the game when the team is having the lead. On the other hand, when the team is
trailing I want to know the probability of coming back under this situation, or even in a game
that is not that close I always wonder whether the game will come down to the wire or not.
These numbers and information sometimes could be estimated by some experienced fan’s
intuition, but for a spectator that does not have that much experience watching the game
would see this information very valuable.
The main product of this project is a dashboard that could let the users interact. The
dashboard could let the users choose the margin of points and time left on the play clock
(20:00, 16:00, 12:00, 8:00, 4:00), then the probability of winning and the game becoming a
close game would come out. The reason I choose these time periods is because these are the
NCAA media timeouts. In this research, the definition of a close game is under 4 minutes and
the margin of points is within four. The probability of the game winning by the home team is
based on logistic regression and the probability of it becoming a close game is based on a 3-
layer neural network. The data I used is all the conference games from the 2023-2024, 2022-
2023, and 2021-2022 seasons. The reason I only used conference games is because these
games are more evenly matched. It will have fewer games that are won by 20 or more points.
so the result of the model is more valuable and accurate.
