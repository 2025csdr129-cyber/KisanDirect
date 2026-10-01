from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime
from app.database import Base

class DBFarmerUser(Base):
    __tablename__ = "farmer_users"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    hashed_pin = Column(String, default="")
    otp_code = Column(String, default="")
    is_verified = Column(Boolean, default=False)
    full_name = Column(String)
    village = Column(String)
    district = Column(String)
    fpo_hub = Column(String)
    land_acres = Column(Float, default=1.0)
    primary_crop = Column(String, default="Tomato")
    upi_id = Column(String, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

class DBProduceListing(Base):
    __tablename__ = "produce_listings"

    id = Column(Integer, primary_key=True, index=True)
    farmer_name = Column(String, index=True)
    phone_number = Column(String, default="N/A")
    fpo_hub_id = Column(String)
    crop = Column(String, index=True)
    grade = Column(String)
    quality_confidence = Column(Float, default=94.5)
    quality_certificate_id = Column(String, default="")
    quantity_kg = Column(Float)
    mandi_benchmark_price = Column(Float)
    is_perishable = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class DBColdStorageBooking(Base):
    __tablename__ = "cold_storage_bookings"

    id = Column(Integer, primary_key=True, index=True)
    farmer_name = Column(String)
    facility_name = Column(String)
    crate_count = Column(Integer)
    days = Column(Integer)
    total_cost = Column(Float)
    status = Column(String, default="CONFIRMED")
    booked_at = Column(DateTime, default=datetime.utcnow)

class DBInputCollectiveOrder(Base):
    __tablename__ = "input_collective_orders"

    id = Column(Integer, primary_key=True, index=True)
    farmer_name = Column(String)
    input_item = Column(String)
    quantity = Column(Integer)
    unit = Column(String)
    pooled_price = Column(Float)
    status = Column(String, default="POOLED_FOR_BACKHAUL")
    created_at = Column(DateTime, default=datetime.utcnow)

class DBEscrowOrder(Base):
    __tablename__ = "escrow_orders"

    id = Column(Integer, primary_key=True, index=True)
    listing_id = Column(Integer)
    buyer_name = Column(String)
    quantity_kg = Column(Float)
    total_amount = Column(Float)
    advance_amount = Column(Float, default=0.0)
    final_amount = Column(Float, default=0.0)
    advance_status = Column(String, default="UNPAID")
    escrow_status = Column(String, default="HOLD")
    payout_channel = Column(String, default="UPI")
    created_at = Column(DateTime, default=datetime.utcnow)
