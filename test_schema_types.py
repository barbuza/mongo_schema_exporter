"""
Unit tests for MongoDB schema exporter.
"""

from schema_types import (
    MongoUnion,
    MongoArray,
    MongoObject,
    MongoString,
    MongoInteger,
    MongoField,
)


def test_mongo_union_flatten() -> None:
    """Test MongoUnion.flatten method."""
    assert MongoUnion(types=[MongoString(), MongoInteger()]).flatten() == MongoUnion(
        types=[MongoString(), MongoInteger()]
    )

    assert MongoUnion(
        types=[MongoString(), MongoUnion(types=[MongoString(), MongoInteger()])]
    ).flatten() == MongoUnion(types=[MongoString(), MongoInteger()])

    assert MongoUnion(types=[]).flatten().__class__.__name__ == "MongoUnknown"


def test_merge_arrays() -> None:
    """Test merge_arrays function."""
    assert MongoArray.merge(
        [MongoArray(element=MongoString())]
    ).flatten() == MongoArray(element=MongoString())
    assert MongoArray.merge(
        [MongoArray(element=MongoString()), MongoArray(element=MongoInteger())]
    ).flatten() == MongoArray(element=MongoUnion(types=[MongoString(), MongoInteger()]))
    assert MongoArray.merge(
        [
            MongoArray(element=MongoString()),
            MongoArray(element=MongoUnion(types=[MongoString(), MongoInteger()])),
        ]
    ).flatten() == MongoArray(element=MongoUnion(types=[MongoString(), MongoInteger()]))


def test_merge_objects() -> None:
    """Test merge_objects function."""
    assert MongoObject.merge(
        [
            MongoObject(
                fields={
                    "a": MongoField(type=MongoString(), required=True),
                    "b": MongoField(type=MongoInteger(), required=True),
                }
            ),
            MongoObject(
                fields={
                    "a": MongoField(type=MongoInteger(), required=True),
                    "c": MongoField(type=MongoString(), required=True),
                }
            ),
        ]
    ).flatten() == MongoObject(
        fields={
            "a": MongoField(
                type=MongoUnion(types=[MongoString(), MongoInteger()]), required=True
            ),
            "b": MongoField(type=MongoInteger(), required=False),
            "c": MongoField(type=MongoString(), required=False),
        }
    )
