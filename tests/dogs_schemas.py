get_random_dog_schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string"},
        },
        "required": ["message", "status"]
    }

get_all_breeds_schema = {
    "type": "object",
    "properties": {
        "message": {
            "type": "object",
            "properties": {
                "affenpinscher": {"type": "array", "items": {"type": "string"}},
                "african": {"type": "array", "items": {"type": "string"}},
                "airedale": {"type": "array", "items": {"type": "string"}},
                "akita": {"type": "array", "items": {"type": "string"}},
                "appenzeller": {"type": "array", "items": {"type": "string"}},
                "australian": {"type": "array", "items": {"type": "string"}},
                "basenji": {"type": "array", "items": {"type": "string"}},
                "beagle": {"type": "array", "items": {"type": "string"}},
                "bluetick": {"type": "array", "items": {"type": "string"}},
                "borzoi": {"type": "array", "items": {"type": "string"}},
                "bouvier": {"type": "array", "items": {"type": "string"}},
                "boxer": {"type": "array", "items": {"type": "string"}},
                "brabancon": {"type": "array", "items": {"type": "string"}},
                "briard": {"type": "array", "items": {"type": "string"}},
                "buhund": {"type": "array", "items": {"type": "string"}},
                "bulldog": {"type": "array", "items": {"type": "string"}},
                "bullterrier": {"type": "array", "items": {"type": "string"}},
                "cattledog": {"type": "array", "items": {"type": "string"}},
                "chihuahua": {"type": "array", "items": {"type": "string"}},
                "chow": {"type": "array", "items": {"type": "string"}},
                "clumber": {"type": "array", "items": {"type": "string"}},
                "cockapoo": {"type": "array", "items": {"type": "string"}},
                "collie": {"type": "array", "items": {"type": "string"}},
                "coonhound": {"type": "array", "items": {"type": "string"}},
                "corgi": {"type": "array", "items": {"type": "string"}},
                "cotondetulear": {"type": "array", "items": {"type": "string"}},
                "dachshund": {"type": "array", "items": {"type": "string"}},
                "dalmatian": {"type": "array", "items": {"type": "string"}},
                "dane": {"type": "array", "items": {"type": "string"}},
                "deerhound": {"type": "array", "items": {"type": "string"}},
                "dhole": {"type": "array", "items": {"type": "string"}},
                "dingo": {"type": "array", "items": {"type": "string"}},
                "doberman": {"type": "array", "items": {"type": "string"}},
                "elkhound": {"type": "array", "items": {"type": "string"}},
                "entlebucher": {"type": "array", "items": {"type": "string"}},
                "eskimo": {"type": "array", "items": {"type": "string"}},
                "finnish": {"type": "array", "items": {"type": "string"}},
                "frise": {"type": "array", "items": {"type": "string"}},
                "germanshepherd": {"type": "array", "items": {"type": "string"}},
                "greyhound": {"type": "array", "items": {"type": "string"}},
                "groenendael": {"type": "array", "items": {"type": "string"}},
                "havanese": {"type": "array", "items": {"type": "string"}},
                "hound": {"type": "array", "items": {"type": "string"}},
                "husky": {"type": "array", "items": {"type": "string"}},
                "keeshond": {"type": "array", "items": {"type": "string"}},
                "kelpie": {"type": "array", "items": {"type": "string"}},
                "komondor": {"type": "array", "items": {"type": "string"}},
                "kuvasz": {"type": "array", "items": {"type": "string"}},
                "labradoodle": {"type": "array", "items": {"type": "string"}},
                "labrador": {"type": "array", "items": {"type": "string"}},
                "leonberg": {"type": "array", "items": {"type": "string"}},
                "lhasa": {"type": "array", "items": {"type": "string"}},
                "malamute": {"type": "array", "items": {"type": "string"}},
                "malinois": {"type": "array", "items": {"type": "string"}},
                "maltese": {"type": "array", "items": {"type": "string"}},
                "mastiff": {"type": "array", "items": {"type": "string"}},
                "mexicanhairless": {"type": "array", "items": {"type": "string"}},
                "mix": {"type": "array", "items": {"type": "string"}},
                "mountain": {"type": "array", "items": {"type": "string"}},
                "newfoundland": {"type": "array", "items": {"type": "string"}},
                "otterhound": {"type": "array", "items": {"type": "string"}},
                "ovcharka": {"type": "array", "items": {"type": "string"}},
                "papillon": {"type": "array", "items": {"type": "string"}},
                "pekinese": {"type": "array", "items": {"type": "string"}},
                "pembroke": {"type": "array", "items": {"type": "string"}},
                "pinscher": {"type": "array", "items": {"type": "string"}},
                "pitbull": {"type": "array", "items": {"type": "string"}},
                "pointer": {"type": "array", "items": {"type": "string"}},
                "pomeranian": {"type": "array", "items": {"type": "string"}},
                "poodle": {"type": "array", "items": {"type": "string"}},
                "pug": {"type": "array", "items": {"type": "string"}},
                "puggle": {"type": "array", "items": {"type": "string"}},
                "pyrenees": {"type": "array", "items": {"type": "string"}},
                "redbone": {"type": "array", "items": {"type": "string"}},
                "retriever": {"type": "array", "items": {"type": "string"}},
                "ridgeback": {"type": "array", "items": {"type": "string"}},
                "rottweiler": {"type": "array", "items": {"type": "string"}},
                "saluki": {"type": "array", "items": {"type": "string"}},
                "samoyed": {"type": "array", "items": {"type": "string"}},
                "schipperke": {"type": "array", "items": {"type": "string"}},
                "schnauzer": {"type": "array", "items": {"type": "string"}},
                "segugio": {"type": "array", "items": {"type": "string"}},
                "setter": {"type": "array", "items": {"type": "string"}},
                "sharpei": {"type": "array", "items": {"type": "string"}},
                "sheepdog": {"type": "array", "items": {"type": "string"}},
                "shiba": {"type": "array", "items": {"type": "string"}},
                "shihtzu": {"type": "array", "items": {"type": "string"}},
                "spaniel": {"type": "array", "items": {"type": "string"}},
                "spitz": {"type": "array", "items": {"type": "string"}},
                "springer": {"type": "array", "items": {"type": "string"}},
                "stbernard": {"type": "array", "items": {"type": "string"}},
                "terrier": {"type": "array", "items": {"type": "string"}},
                "tervuren": {"type": "array", "items": {"type": "string"}},
                "vizsla": {"type": "array", "items": {"type": "string"}},
                "waterdog": {"type": "array", "items": {"type": "string"}},
                "weimaraner": {"type": "array", "items": {"type": "string"}},
                "whippet": {"type": "array", "items": {"type": "string"}},
                "wolfhound": {"type": "array", "items": {"type": "string"}}
            },
            "additionalProperties": False
        },
        "status": {"type": "string"}
    },
    "required": ["message", "status"],
    "additionalProperties": False
}

get_dog_by_breed_schema = {
  "type": "object",
  "properties": {
    "message": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "status": {
      "type": "string"
    }
  },
  "required": ["message", "status"]
}

get_all_sub_breeds_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "array"},
        "status": {"type": "string"},
    },
    "required": ["message", "status"]
}

get_random_dog_by_breed_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "status": {"type": "string"},
    },
    "required": ["message", "status"]
}
