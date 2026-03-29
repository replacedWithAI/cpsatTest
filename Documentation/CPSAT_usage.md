There's an entire book on CPSAT so I'll oversimplify
[I followed the guide here; might be more followable](https://d-krupke.github.io/cpsat-primer/04B_advanced_modelling.html#scheduling-for-multiple-resources-with-optional-intervals)

What's CPSAT?
A linear programming, constraint programming solver, which I'll use for scheduling

# Functions/classes

## Add_courses_to_CPSAT / Make_CPSAT_variables
Idea:
Each class (the whole thing) of each section has one set of timeslots to choose from
Therefore, each class's timeslots need to be toggeable
So, each timeslot must be its own bool variable
Keep in mind: is_present makes intervals toggleable. To decide how they'll be toggled, decide later

### Relevance/importance
You see me using a bunch of loops and dictionaries when defining these variables
These don't really matter; the interval variables only care about:
- the start time numerical values
- any CPSAT boolean variable
The loops are only for assigning keys to these values. Could've just put them in a list

### Definitions

#### Start_time variables
These are when the interval starts in the schedule
Their data type is CPSAT_obj.new_int_var_from_domain
They need CPSAT_obj.Domain.from_intervals(int) arguments, the int being the numerical start time

#### Is_present variables
Lets an interval be present or not
Their data type is CPSAT_obj.new_bool_var
It's just a CPSAT boolean variable; no arguments or algorithms needed

#### Interval variable
Each lecture, lab, tutorial is an interval variable. These variables have:
- start_time variables
- size variables, which is just the class duration (int)
- is_present variables
- name variables; what they're called (string)

## add_constraints / Add_CPSAT_constraints
This adds rules for the scheduler to follow
The rules I'll add are:
- Intervals can't overlap; maybe I'll let people decide a degree of overlap
- One section per course
- One lab/tutorial per course, if applicable
- Don't take classes in specified times

Also groups interval variables in a seperate dictionary, where each weekday is the key
This'll be used for solving for scheduling objectives
