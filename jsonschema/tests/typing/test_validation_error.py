"""
This module tests that type checkers allow `ValidationError.validator` to be
`str | None` (as produced by boolean false schemas).
"""

from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError

error = ValidationError("message", validator=None)
validator: str | None = error.validator

e = next(
    iter(
        Draft202012Validator({"properties": {"a": False}}).iter_errors(
            {"a": 1},
        ),
    ),
)
err_validator: str | None = e.validator

# Ensure that validator is not inferred as just 'str'
str_var: str
str_var = error.validator  # type: ignore[assignment]
