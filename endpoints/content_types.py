from ..base import ClientBase


class TypesContentClient(ClientBase):
    endpoint = '/types'

    def _types(self, operation,
               fields='all', from_record=1, to_record=100,
               lang=None, use_second_lang=None, last_update=None,
               code=None):
        payload = {'language': lang,
                   'useSecondaryLanguage': use_second_lang,
                   'from': from_record,
                   'to': to_record,
                   'lastUpdateTime': last_update,
                   'code': code}
        if isinstance(fields, basestring):
            payload.update({'fields': fields})
        else:
            payload.update({'fields': ','.join(fields)})
        return self.transport.get(
                        self._url(operation),
                        params=payload)

    def accommodations(self, fields='all', from_record=1, to_record=100,
                       lang='ENG', use_second_lang=False):
        return self._types(operation='accommodations',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang)

    def boards(self, fields='all', from_record=1, to_record=100,
               lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='boards',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def categories(self, fields='all', from_record=1, to_record=100,
                   lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='categories',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def chains(self, fields='all', from_record=1, to_record=100,
               lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='chains',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def ratecomments(self, fields='all', from_record=1, to_record=100,
                     lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='ratecomments',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def currencies(self, fields='all', from_record=1, to_record=100,
                   lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='currencies',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def facilities(self, fields='all', from_record=1, to_record=100,
                   lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='facilities',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def facilitygroups(self, fields='all', from_record=1, to_record=100,
                       lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='facilitygroups',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def facilitytypologies(self, from_record=1, to_record=100,
                           lang='ENG', last_update=None):
        return self._types(operation='facilitytypologies',
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           last_update=last_update)

    def issues(self, fields='all', from_record=1, to_record=100,
               lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='issues',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def languages(self, fields='all', from_record=1, to_record=100,
                  lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='languages',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def promotions(self, fields='all', from_record=1, to_record=100,
                   lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='promotions',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def rooms(self, fields='all', from_record=1, to_record=100,
              lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='rooms',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def segments(self, fields='all', from_record=1, to_record=100,
                 lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='segments',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def terminals(self, fields='all', from_record=1, to_record=100,
                  lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='terminals',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def imagetypes(self, fields='all', from_record=1, to_record=100,
                   lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='imagetypes',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def groupcategories(self, fields='all', from_record=1, to_record=100,
                        lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='groupcategories',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update)

    def ratecommentdetail(self, code, fields='all',
                          from_record=1, to_record=100,
                          lang='ENG', use_second_lang=False, last_update=None):
        return self._types(operation='ratecommentdetail',
                           fields=fields,
                           from_record=from_record,
                           to_record=to_record,
                           lang=lang,
                           use_second_lang=use_second_lang,
                           last_update=last_update,
                           code=code)
