# Airline Demand Forecast 

## Problem Description 

### Demand Forecasting

- Critical component of airline revenue management

10% increase in forecasting accuracy may result in 3% increase in revenue.

- Approaches to demand forecasting

Advance Booking Model

Time-series Model

Combined Model

## Data 

- Training Data

84 departure dates

61 days prior (days prior=0,1,…,60)

- Validation Data

7 departure dates (7/25~7/31)

29 days prior (days prior=0,1,…,28)

Naïve forecasts

## Forecasting Model

### Advance Booking Model

- Widely adopted in travel industry

- Performs quite well in short-term forecasting
Especially for days prior < 4 weeks

- Based on two information

Booking curve : Estimated from historical bookings

Bookings-on-hand (on-the-book): cumulative bookings at the given booking date 

- Multiplicative Model

Forecast = on-the-book/(historical booking rate for given days prior)

E.g. historical average booking rate for days prior=8…365 = 50%

Final forecast = 80/0.5 = 160

## Purpose of the project

- Apply booking pattern estimated from training data into validation data

- Compute final demand forecasts for 7 departure dates and days prior 1…28 (validation data)

- minimize forecast errors.

## Minimize forecast by minimizing Mean Absolute Scaled Error

Example:

Total absolute error of naïve forecasts: 5837
E.g. total absolute error of your model: 3000 
MASE=3000/5837 = 51.3%
Forecast error of your model is 51.3% of that of benchmark.
You reduced errors by 48.7%!

Measure forecast errors for days prior 1,…., 28 (Do not include days prior =0)

## Summary Write up of Goal Achieved

Multiplicative model performed along with smoothing.Rolling average on the multiplicative model to smooth out 
the multiplicative model giving a better mean absolute squared error. Firstly I created my multiplicative model. 
The steps involved were as follows: Step1: Booking rate was calculated by take the proportion of cumulative demand 
from the final demand for each prior day for each departure date in the training data set. Step2. The booking rate 
for each of the prior days were averaged. Step3. Using the average booking rate we got from the training data set. 
I divided the cumulative bookings for each prior dates for each departure date in the validation data set by the 
average booking rate we got from the training data set. Afterwards, the validation data set was sorted in ascending 
order of departure date with booking date to make sure the smoothing was done in the right order. The smoothing takes 
place in period of 28 days. So, the multiplicative forecast for 28th prior day stay the same for the 28th day. 
For the 27th prior day, the average of the 28th and 27th day is taken. For the 26th  prior day, the average of the 28th,
27th and 26th day is taken and so forth and so on. This ensures that the future is always an average of the past. 
The MASE after removing the 0 prior days give .75 which is still better than .83 with only the multiplicative model alone.
