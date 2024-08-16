This is a submission for the 'Demcon Festival Schedule Generator' challenge.

The goal of the program is to find a feasible assignment of shows to stages,
such that no stage has two shows at the same time, minimizing the number
of stages. The shows have a defined beginning and end time.

We use a simple sweep-line algorithm with start and end events for each show.

The software will read the input from the standard input. It needs to be of the form
as given in the example file.
The software will display the assignment in human-readable form on the standard output
and it will display a chart of the resulting assignment.

To run the software, any recent Python version with matplotlib in its environment should suffice.

        $ python demcon_planner.py < example_in

If you want to have a separate environment and don't have matplotlib installed, please run

        $ conda env create -n demcon-challenge -f ./environment.yaml 
        $ conda activate demcon-challenge
        $ python demcon_planner.py < example_in

Since this is a programming puzzle, no robustness is implemented nor has automated testing been done.

Jochem Berndsen, Aug 15, 2024, jochem@functor.nl

