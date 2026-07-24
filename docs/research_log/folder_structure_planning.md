# Folder Structure

Plots: what am I actually doing?

**Running to a time : 0.5, 1, 2, 3 , 15.**

**Values of M: 2 to 10.**

1. Initial Checkpoint error:
    - Multistream with exact moment function
2. Final checkpoint error:
    - multistream with exact moment function
    - multistream with 2d moment

Running for M = 2, 4, 5, 10, 15.

T = [0.01,0.02…5s] - ylog.

1. plot the initial checkpoint error: multistream vs exact moment
2. plot the final checkpoint error: multistream vs 2d

The files I need:

M = 2 to 10, checkpointed at T = [0.5,1,2,3] : run simulation for this.

M = 2,4, 5, 10, 15: checkpointed at T = [0.01, 0.02,…..]

Make M,T pairs and run for those, honestly, Sania. It's not that hard.

pair folder like M_T_ and access them- best!

also have M initial checkpoint- like, initial_cp/M_i
