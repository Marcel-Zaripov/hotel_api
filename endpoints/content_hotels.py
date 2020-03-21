from ..base import ClientBase


class HotelsContentClient(ClientBase):
    endpoint = '/hotels'

    def list_hotels_content(self,
                            fields=None, hotel_codes=None,
                            destination_code=None, country_code=None,
                            last_update=None, lang=None,
                            from_record=None, to_record=None,
                            use_second_lang=False):
        """
        :param fields: list
                       fields to be included in response
                       if None all fields are included
                       Available fields:
                            name
                            description
                            countryCode
                            destinationCode
                            zoneCode
                            coordinates
                            categoryCode
                            chainCode
                            license
                            address
                            postalCode
                            city
                            email
                            giataCode
                            accommodationTypeCode
                            phones
                            rooms
                            images
                            boardCodes
                            facilities
                            segmentCodes
                            web
                            terminals
                            issues
                            interestPoints
                            wildcards
        :param hotel_codes: list
                            filter for specific list of hotels
        :param destination_code: str
                                 filter for specific destination
        :param country_code: str
                             filter for specific country
        :param last_update: str
                            date in iso format
        :param lang: str
                         three letter language code, e.g. 'ENG'
        :param from_record: int
                            initial record to receive
        :param to_record: int
                          final record to receive
        :param use_second_lang: bool
                                whether to use fallback language (English)
        :return: json response
        """
        payload = {}
        if fields:
            payload.update({'fields': ','.join(fields)})
        if hotel_codes:
            payload.update({'codes': ','.join(hotel_codes)})
        if destination_code:
            payload.update({'destinationCode': destination_code})
        if country_code:
            payload.update({'countryCode': country_code})
        if last_update:
            payload.update({'lastUpdateTime': last_update})
        if lang:
            payload.update({'language': language})
        if from_record:
            payload.update({'from': from_record})
        if to_record:
            payload.update({'to': to_record})
        if use_second_lang:
            payload.update({'useSecondaryLanguage': use_second_lang})
        return self.transport.get(self._url(), params=payload)

    def get_hotel_details(self, hotel_code,
                          lang=None, use_second_lang=None):
        """
        :param hotel_code: str
                           inner hotel code
        :param lang: str
                         three letter language code, e.g. 'ENG'
        :param use_second_lang: bool
                                whether to use fallback language (English)
        :return: json response
        """
        payload = {}
        if lang:
            payload.update({'language': lang})
        if use_second_lang:
            payload.update({'useSecondaryLanguage': use_second_lang})
        return self.transport.get(self._url(hotel_code), params=payload)
