get_all_posts_schema = {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "userId": {"type": "integer"},
      "id": {"type": "integer"},
      "title": {"type": "string"},
      "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
  }
}

get_post_by_id_schema = {
  "type": "object",
  "properties": {
    "id": {"type": "integer"},
    "userId": {"type": "integer"},
    "title": {"type": "string"},
    "body": {"type": "string"}
  },
  "required": ["userId", "id", "title", "body"]
}

create_and_update_post_schema = {
  "type": "object",
  "properties": {
    "id": {"type": "integer"},
    "title": {"type": "string"},
    "body": {"type": "string"},
    "userId": {"type": "string"}
  },
  "required": ["title", "body", "userId"]
}

get_all_post_by_user_shema = {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "userId": {
        "type": "integer"
      },
      "id": {
        "type": "integer"
      },
      "title": {
        "type": "string"
      },
      "body": {
        "type": "string"
      }
    },
    "required": ["userId", "id", "title", "body"]
  }
}



