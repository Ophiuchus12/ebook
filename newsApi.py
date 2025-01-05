from newsapi import NewsApiClient

def main():
    api = NewsApiClient(api_key='5010a71dced34e72b261fecd0cb830f3')

    result = api.get_everything(q='bitcoin', language='en')
    print(result)
    return result

if __name__ == "__main__":
    main()
