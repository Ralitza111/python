# Predicting tomorrow’s weather Naïve time series forecasting

## Input data

- Weather record of the last n days. 0s(no rain) and 1s(rain).

- k: number of records (days) to use for producing forecasts. 

- Example, k=3, input data = [1,0,1,0,1]

## Processing

### Part1: Naïve time series forecasting

- Forecast will be 1 if the number of 1s in the previous k time periods is at least k/2 0 otherwise

### Part2: Forecasting error

- MAE: mean absolute error = average of |actual - forecast |

- Example, k=3, input data = (1,0,1,0,1)

- Forecast for period 4: 1 (since 1+0+1 >= 1.5), absolute error= |0-1|=1

- Forecast for period 5: 0 (since 0+1+0 < 1.5), absolute error= |1-0|=1

- MAE= 1



## Output

- MAE: mean absolute error

## Function “naivePrediction(lyst,k)”

- Input : list of 0s and 1s, k (number of periods to use)

- Output: MAE

- If the number of observations is less than or equal to k, print error message.
