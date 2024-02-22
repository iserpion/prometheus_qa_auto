import requests


class SpaceX():
    """Class holds method to send query to fake SpaceX GraphQL API"""

    url = 'https://spacex-production.up.railway.app/'

    def send_qraphql_query(self, query):
        response = requests.post(self.url, json={'query': str(query)})

        return response
    