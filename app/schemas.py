from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from enum import Enum
from datetime import datetime

class ProduceGrade(str, Enum):
    GRADE_A = "Grade A"
    GRADE_B = "Grade B"
    GRADE_C = "Grade C"

class RequestOTPRequest(BaseModel):
    phone_number: str

class VerifyOTPRequest(BaseModel):
    phone_number: str
    otp_code: str

class SetPinRequest(BaseModel):
    phone_number: str
    new_pin: str

class FarmerLoginRequest(BaseModel):
    phone_number: str
    pin: str

class FarmerRegisterRequest(BaseModel):
    phone_number: str
    pin: str
    full_name: str
    village: str
    district: str
    fpo_hub: str
    land_acres: float
    primary_crop: str
    upi_id: Optional[str] = ""

class ProduceListingBase(BaseModel):
    farmer_name: str
    fpo_hub_id: str
    crop: str
    grade: ProduceGrade
    quality_confidence: Optional[float] = 95.0
    quality_certificate_id: Optional[str] = ""
    quantity_kg: float
    mandi_benchmark_price: float
    is_perishable: bool = True
    phone_number: Optional[str] = "N/A"

class ProduceListingCreate(ProduceListingBase):
    pass

class ProduceListing(ProduceListingBase):
    id: int
    created_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

class ColdStorageRequest(BaseModel):
    farmer_name: str
    facility_name: str
    crate_count: int
    days: int

class InputOrderRequest(BaseModel):
    farmer_name: str
    input_item: str
    quantity: int
    unit: str

class PriceCorridorResponse(BaseModel):
    crop: str
    mandi_benchmark: float
    recommended_farmer_price: float
    recommended_consumer_price: float
    intermediary_savings_retained: float

class LogisticsNode(BaseModel):
    id: int
    name: str
    node_type: str
    demand_kg: float
    lat: float
    lng: float
    is_perishable: bool = False

class CircularOptimizationRequest(BaseModel):
    vehicle_capacity_kg: float
    nodes: List[LogisticsNode]

class EscrowOrderCreate(BaseModel):
    listing_id: int
    buyer_name: str
    quantity_kg: float
    unit_price: float
