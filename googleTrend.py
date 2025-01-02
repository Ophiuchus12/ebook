from pytrends.request import TrendReq
import pandas as pd

def trendGlobal():
    # Connexion à PyTrends
    pytrends = TrendReq(hl='en-US', tz=360)

    # Obtenir les recherches tendance mondiales
    global_trending = pytrends.trending_searches(pn='united_states')

    trend_names = global_trending[0].tolist()

    for trend in trend_names : 
        print(trend)

    return trend_names

def interestSubject7days():
    pytrends = TrendReq(hl='en-US', tz=360)

    list= trendGlobal()
    trend_names1 = list[:5]
    trend_names2 = list[5:10]

    pytrends.build_payload(trend_names1, timeframe='today 1-m', geo='US')

    interest_over_time1 = pytrends.interest_over_time()

    pytrends.build_payload(trend_names2, timeframe='today 1-m', geo='US')

    interest_over_time2 = pytrends.interest_over_time()

    all_interest = pd.concat([interest_over_time1, interest_over_time2], axis=1)

    print(all_interest)

    all_interest.to_csv('trends_week.csv', index=True)




if __name__ == "__main__":
    interestSubject7days()