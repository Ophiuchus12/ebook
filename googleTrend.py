from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime
import os
import time 

pd.set_option('future.no_silent_downcasting', True)
def nowdate():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


def trendGlobal():
    # Connexion à PyTrends
    pytrends = TrendReq(hl='en-US', tz=360)

    # Obtenir les recherches tendance mondiales
    global_trending = pytrends.trending_searches(pn='united_states')

    if global_trending.empty:
        print("Aucune tendance globale retournée. Vérifiez la région ou réessayez plus tard.")
        return None


    trend_names = global_trending[0].tolist()

    # for trend in trend_names : 
    #     print(trend)

    return trend_names

def interestSubject():
    pytrends = TrendReq(hl='en-US', tz=360)

    # Récupérer la liste globale
    list = trendGlobal()
    if not list:
        return None 

    # Découper la liste en deux parties
    trend_names1 = list[:5]
    trend_names2 = list[5:10]

    print("Liste 1:", trend_names1, "Liste 2:", trend_names2)

    try:
        # Traitement pour trend_names1
        pytrends.build_payload(trend_names1, timeframe='today 1-m', geo='US')
        interest_over_time1 = pytrends.interest_over_time()

        # Traitement pour trend_names2
        pytrends.build_payload(trend_names2, timeframe='today 1-m', geo='US')
        interest_over_time2 = pytrends.interest_over_time()

        # Concaténer les deux DataFrames
        all_interest = pd.concat([interest_over_time1, interest_over_time2], axis=1)

        # Vérifier et supprimer la colonne 'isPartial'
        if 'isPartial' in all_interest.columns:
            all_interest = all_interest.drop(columns=['isPartial'])

        # Calculer la somme pour chaque colonne (chaque sujet) et trier
        total_interest = all_interest.sum().sort_values(ascending=False)
        print(total_interest)

        # Retourner les 5 premiers éléments
        return total_interest[:5]

    except Exception as e:
        # Gestion d'erreur : renvoyer les 5 premiers sujets en cas de problème
        print(f"Une erreur est survenue : {e}", trend_names1)
        return trend_names1


    # output_dir = 'csvTrend'
    # if not os.path.exists(output_dir):
    #     os.makedirs(output_dir)

    # file_name = os.path.join(output_dir, f'trends_week_{nowdate()}.csv')
    # all_interest.to_csv(file_name, index=True)

    # print(f"Fichier enregistré sous le nom : {file_name}")



if __name__ == "__main__":
    interestSubject()