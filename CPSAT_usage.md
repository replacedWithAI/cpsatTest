There's an entire book on CPSAT so I'll oversimplify
[I followed the guide here; might be more followable](https://d-krupke.github.io/cpsat-primer/04B_advanced_modelling.html#scheduling-for-multiple-resources-with-optional-intervals)

# Add_courses_to_CPSAT
Each lecture, lab, tutorial is an interval variable. These variables have:
- start_time variables
- size variables, which is just the class duration (int)
- is_present variables
- name variables; what they're called (string)

## Start_time variables
These are when the interval starts in the schedule
Their data type is CPSAT_obj.new_int_var_from_domain
They need CPSAT_obj.Domain.from_intervals(int) arguments, the int being the numerical start time

## Is_present variables
Lets an interval be present or not
It's just a CPSAT boolean variable; no arguments or algorithms needed