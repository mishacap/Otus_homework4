get_list_of_breweries_schema = {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {"type": "string"},
      "name": {"type": "string"},
      "brewery_type": {"type": "string"},
      "address_1": {"type": ["string", "null"]},
      "address_2": {"type": ["string", "null"]},
      "address_3": {"type": ["string", "null"]},
      "city": {"type": "string"},
      "state_province": {"type": "string"},
      "postal_code": {"type": "string"},
      "country": {"type": "string"},
      "longitude": {"type": ["string", "null"]},
      "latitude": {"type": ["string", "null"]},
      "phone": {"type": ["string", "null"]},
      "website_url": {"type": ["string", "null"]},
      "state": {"type": "string"},
      "street": {"type": ["string", "null"]}
    },
    "required": ["id", "name", "brewery_type", "address_1", "city", "state_province", "postal_code", "country", "state", "street"]
  }
}

get_single_brewery_by_id_schema = {
  "type": "object",
  "properties": {
    "id": {"type": "string"},
    "name": {"type": "string"},
    "brewery_type": {"type": "string"},
    "address_1": {"type": ["string", "null"]},
    "address_2": {"type": ["string", "null"]},
    "address_3": {"type": ["string", "null"]},
    "city": {"type": "string"},
    "state_province": {"type": "string"},
    "postal_code": {"type": "string"},
    "country": {"type": "string"},
    "longitude": {"type": ["string", "null"]},
    "latitude": {"type": ["string", "null"]},
    "phone": {"type": ["string", "null"]},
    "website_url": {"type": ["string", "null"]},
    "state": {"type": "string"},
    "street": {"type": ["string", "null"]}
  },
  "required": ["id", "name", "brewery_type", "address_1", "city", "state_province", "postal_code", "country", "state", "street"]
}


