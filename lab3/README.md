# Lab 3 (or 9)

So I've basically just started by implementing the most basic evolutionary algorithm with selection, recombination and mutation.
I managed to solve the problem 1 very quickly, but problem 2, 5 and 10 almost seemed to stop at 0.50 percent. So I decided that I would
do some other types of crossover functions and maybe tweak the mutation rate a bit. I also later added the chance of two parents not making
a decendant but instead continuing to the next generation themselves.

## The code

The selection is just textbook stuff, getting k random individuals and
choosing the best one and adding it to the list, and do this n=pop_size times. Crossover is just some basic functions like 1-cut crossover,
2-cut crossover and finally some more experimental stuff. Could definetaly try more stuff there. The mutation is just going through every bit
and randomly flipping them. I also tried that the mutations would affect not only one bit itself, but also the bits around it, with some "spread".
I didn't exactly work as good as I would hope.

## Results

The best I got on any of these tries was end fitness of about 50% for both 2, 5 and 10. And it seemed like the genomes converged to some local optimum
and never managed to get out of it. I should definately try to add some kind of randomness into to try to get it over the "hump". The best results are in the
report.
