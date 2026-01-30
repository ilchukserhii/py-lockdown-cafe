from datetime import date
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = date.today()
        vaccine_expiration_date = (
            visitor.get("vaccine", {}).get("expiration_date")
        )
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")
        elif vaccine_expiration_date < today:
            raise OutdatedVaccineError("OutdatedVaccineError")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError")
        else:
            return f"Welcome to {self.name}"
