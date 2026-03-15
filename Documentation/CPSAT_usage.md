There's an entire book on CPSAT so I'll oversimplify
[I followed the guide here; might be more followable](https://d-krupke.github.io/cpsat-primer/04B_advanced_modelling.html#scheduling-for-multiple-resources-with-optional-intervals)

# Add_courses_to_CPSAT
Each lecture, lab, tutorial is an interval variable. These variables have:
- start_time variables
- size variables, which is just the class duration (int)
- is_present variables
- name variables; what they're called (string)

## Relevance/importance
You see me using a bunch of loops and dictionaries when defining these variables
These don't really matter; the interval variables only care:
- about the start time numerical values
- any CPSAT boolean variable

The loops are only for assigning keys to these values. Could've just put them in a list

### Start_time variables
Their values will only be a numerical start time

## Definitions

### Start_time variables
These are when the interval starts in the schedule
Their data type is CPSAT_obj.new_int_var_from_domain
They need CPSAT_obj.Domain.from_intervals(int) arguments, the int being the numerical start time

### Is_present variables
Lets an interval be present or not
Their data type is CPSAT_obj.new_bool_var
It's just a CPSAT boolean variable; no arguments or algorithms needed

### Interval
