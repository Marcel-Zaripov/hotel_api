from ..base import ClientBase


class LocationsContentClient(ClientBase):
    endpoint = '/locations'

    def _locations(self, operation,
                   fields='all', lang='ENG', use_second_lang=False,
                   from_record=1, to_record=100, last_update=None,
                   destination_codes=None, country_codes=None):
        country_codes_field = 'codes'
        if operation == 'destinations':
            country_codes_field = 'countryCodes'
        payload = {'language': lang,
                   'useSecondaryLanguage': use_second_lang,
                   'from': from_record,
                   'to': to_record,
                   'lastUpdateTime': last_update}
        if isinstance(fields, basestring):
            payload.update({'fields': fields})
        else:
            payload.update({'fields': ','.join(fields)})
        if country_codes:
            if isinstance(country_codes, basestring):
                payload.update(
                        {country_codes_field: country_codes})
            else:
                payload.update(
                        {country_codes_field: ','.join(country_codes)})
        if destination_codes:
            if isinstance(destination_codes, basestring):
                payload.update({'codes': destination_codes})
            else:
                payload.update({'codes': ','.join(destination_codes)})
        return self.transport.get(
                        self._url(operation),
                        params=payload)

    def countries(self, fields='all', lang='ENG', use_second_lang=False,
                  from_record=1, to_record=100, last_update=None,
                  country_codes=None):
        """
        :param fields: str or list
                       if str - comma separated list of fields:
                       name,countryCode,isoCode,zones,groupZones
        :param lang: str
                         three letter language code, e.g. 'ENG'
        :param use_second_lang: bool
                                whether to use fallback language (English)
        :param from_record: int
                            initial record to receive
        :param to_record: int
                          final record to receive
        :param last_update: str
                            date in iso format
        :param country_codes: str or list
                              2 letter country codes like 'UK'
                              if provided in str separate with comma:
                              'UK,US,ES'
        :return: json response
        """
        return self._locations(
                        operation='countries',
                        fields=fields,
                        lang=lang,
                        use_second_lang=use_second_lang,
                        from_record=from_record,
                        to_record=to_record,
                        last_update=last_update,
                        country_codes=country_codes)

    def destinations(self, fields='all', lang='ENG', use_second_lang=False,
                     from_record=1, to_record=100, last_update=None,
                     country_codes=None, destination_codes=None):
        """
        :param fields: str or list
                       if str - comma separated list of fields:
                       name,countryCode,isoCode,zones,groupZones
        :param lang: str
                         three letter language code, e.g. 'ENG'
        :param use_second_lang: bool
                                whether to use fallback language (English)
        :param from_record: int
                            initial record to receive
        :param to_record: int
                          final record to receive
        :param last_update: str
                            date in iso format
        :param destination_codes: str or list
                                  platform specific destination codes
                                  'LON' for London, etc.
                                  if provided in str separate with comma:
                                  'LON,NYC,BCN'
        :param country_codes: str or list
                              2 letter country codes like 'UK'
                              if provided in str separate with comma:
                              'UK,US,ES'
        :return: json response
        """
        return self._locations(
                        operation='destinations',
                        fields=fields,
                        lang=lang,
                        use_second_lang=use_second_lang,
                        from_record=from_record,
                        to_record=to_record,
                        last_update=last_update,
                        country_codes=country_codes,
                        destination_codes=destination_codes)
