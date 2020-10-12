# -*- coding: utf-8 -*-

from odoo import models, fields
from ..mapbox import connector


class Location(models.Model):
    _name = 'test.location'
    _description = 'Place location'
    _rec_name = 'place_name'

    place_name = fields.Char(string='Place_name', required=True)
    coordinates = fields.Char(string='Coordinates')
    city = fields.Char(string='City')
    country = fields.Char(string='Country')

    def search(self, args, offset=0, limit=None, order=None, count=False):
        search_result = models.Model.search(self, args, offset, limit, order, count)

        if args and not search_result:
            search_query = args[0][2]
            mapbox_result = connector.search_in_mapbox(search_query)
            mapbox_result = mapbox_result.get('features')
            if mapbox_result:
                coordinates = mapbox_result[0]['geometry']['coordinates']
                coordinates = ', '.join(map(str, coordinates))
                context = mapbox_result[0]['context']
                city = [area['text'] for area in context if area['id'].startswith('place.')]
                city = city[0] if city else None
                country = [area['text'] for area in context if area['id'].startswith('country.')]
                country = country[0] if country else None

                search_result = self.create([{
                    'place_name': search_query.capitalize(),
                    'coordinates': coordinates,
                    'city': city,
                    'country': country
                }])
        return search_result
