from pydantic import BaseModel, ConfigDict


class KoyebModel(BaseModel):
    def __str__(self) -> str:
        return super().model_dump_json(indent=4, exclude_none=True)

    model_config = ConfigDict(
        use_enum_values=True,
        extra="allow",
        validate_assignment=True,
        frozen=True,
        populate_by_name=True,
        arbitrary_types_allowed=True,
        defer_build=True,
    )
