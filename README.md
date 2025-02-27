# MongoDB Schema Exporter

A tool to analyze MongoDB collections and generate schema definitions.

## Features

- Infers schema from MongoDB collections
- Validate documents against generated schemas

## Usage

```bash
# Basic usage
uvx mongo_schema_exporter --db your_database --collection your_collection

# Analyze multiple documents
uvx mongo_schema_exporter --db your_database --collection your_collection --limit 10

# Output as JSON Schema
uvx mongo_schema_exporter --db your_database --collection your_collection --output json

# Save output to a file
uvx mongo_schema_exporter --db your_database --collection your_collection --output json --output-file schema.json

# Connect to a remote MongoDB instance
uvx mongo_schema_exporter --uri "mongodb://user:password@hostname:port/" --db your_database --collection your_collection

# Validate documents against the generated schema
uvx mongo_schema_exporter --db your_database --collection your_collection --validate
```

## Examples

### Pretty-printed output

```python
MongoObject(fields={
    'name': MongoField(type=MongoString(), required=True),
    'age': MongoField(type=MongoInteger(), required=False),
    'tags': MongoField(type=MongoArray(element=MongoString()), required=True),
    'metadata': MongoField(type=MongoObject(fields={
        'created': MongoField(type=MongoDate(), required=True),
        'modified': MongoField(type=MongoDate(), required=False)
    }), required=False)
})
```

### JSON Schema output

```json
{
  "$jsonSchema": {
    "bsonType": "object",
    "properties": {
      "name": {
        "bsonType": "string"
      },
      "age": {
        "bsonType": "int"
      },
      "tags": {
        "bsonType": "array",
        "items": {
          "bsonType": "string"
        }
      },
      "metadata": {
        "bsonType": "object",
        "properties": {
          "created": {
            "bsonType": "date"
          },
          "modified": {
            "bsonType": "date"
          }
        },
        "required": ["created"]
      }
    },
    "required": ["name", "tags"]
  }
}
```

## License

MIT
