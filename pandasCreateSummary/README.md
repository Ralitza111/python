# Summarizing a numeric variable by group

function generateNumericSummary with the following specification:

## Input

-dat: numerical (pandas) Series

-group: categorical (pandas) Series of the same length as  dat

## Output: a dictionary of following elements

-“numMissing” : the number of values of  dat  that are missing

Data type: integer

-“mean” : means of  dat  across the different levels of  groups

Data type: pandas Series

-“std” : standard deviations of  dat  across the different levels of  groups

Data type: pandas Series
