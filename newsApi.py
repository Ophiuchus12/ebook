from newsapi import NewsApiClient

def main():
    response = []
    api = NewsApiClient(api_key='5010a71dced34e72b261fecd0cb830f3')

    result = api.get_top_headlines(country='us')
    if result['status'] == 'ok':
        articles = result.get('articles', [])
        for index, article in enumerate(articles, start=1):
            title = article.get('title', 'Titre non disponible')
            description = article.get('description', 'Description non disponible')
            response.append({'index': index, 'title': title, 'description': description})
            
    else:
        print("Erreur lors de la récupération des articles.")

    print("response", response[:5])

if __name__ == "__main__":
    main()
