#Author:Ralitza Mondal
import pandas as pd
   
def daysPrior(dataframe):
    dataframe['days_prior'] = (pd.to_datetime(dataframe['departure_date']) - pd.to_datetime(dataframe['booking_date']))
    return dataframe
    

def avg_bookingRate(train_with_Maxdemand):
    train_with_Maxdemand['booking_rate'] = ((train_with_Maxdemand['cum_bookings_x']) / (train_with_Maxdemand['cum_bookings_y'])) 
    avg_rate = train_with_Maxdemand[['departure_date', 'days_prior', 'booking_rate']].groupby(['days_prior']).mean()
    return avg_rate


def Merge(mergeby,df_valid):
    valid1 = df_valid.merge(mergeby, left_on='days_prior',right_index=True)
    return valid1


def MultiplicativeRollingAvg(df_valid):
    df_valid.sort_values(['departure_date',"booking_date"],ascending=True)
    print(df_valid)
    df_valid['multi_forecast'] = ((df_valid['cum_bookings']) / (df_valid['booking_rate'])) 
    df_valid['rolling_avg'] = df_valid.groupby(["departure_date"])["multi_forecast"].transform(lambda x: x.rolling(28, 1).mean())
    
    
    return (df_valid['rolling_avg'])


def MASE(naive,WhichModel,df_valid,abs_err_model):
    
    df_valid[abs_err_model] = abs(((df_valid['final_demand']) - (WhichModel)))
    df_valid['absolute_error_naive'] = abs(((df_valid['final_demand']) - (naive)))


    sum_num = df_valid[abs_err_model].sum()
    sum_denom = df_valid['absolute_error_naive'].sum() 
    mase_model = sum_num / sum_denom
    
    return mase_model

def airlineForecast(training,valid):
    
    train=daysPrior(training)
    valid=daysPrior(valid)
    
    Maxdemand = train.loc[train['days_prior'] == '0 days', ['departure_date', 'cum_bookings']]
    train_with_Maxdemand = train.merge(Maxdemand, left_on='departure_date', right_on='departure_date')
    

    
    valid=Merge(avg_bookingRate(train_with_Maxdemand),valid)

    valid=valid.sort_values(['departure_date',"booking_date"],ascending=True)
    MultiplicativeRollingAvg(valid)
    
    days_0 = valid[valid['days_prior'] == '0 days'].index
    valid.drop(days_0, inplace=True)
    
    df=valid[["departure_date","booking_date","days_prior","naive_forecast","multi_forecast","final_demand","rolling_avg"]]
    print(df.sort_values(['departure_date',"days_prior"]))
    
    return       MASE(valid['naive_forecast'],valid['rolling_avg'],valid,"absolute_error_multi")

def main():
    training = pd.read_csv('airline_booking_trainingData.csv', sep=',', header=0)
    valid = pd.read_csv('airline_booking_validationData.csv', sep=',', header=0)
    return airlineForecast(training,valid)