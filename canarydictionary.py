class canarydictionary:
    canarias = {}

    def __init__(self):
        self.canarias['millo'] = 'maiz'
        self.canarias['papa'] = 'patata'
        self.canarias['baifo'] = 'cabra'
        self.canarias['godo'] = 'miguel'
        self.canarias['guagua'] = 'bus'

    def searchword(self, word):
        if word in self.canarias:
            return self.canarias[word]

        return None
