import math
from typing import Dict, Any, List
from datetime import datetime

class FreightEstimatorService:
    # Baseline freight tariffs from Chennayyagunta/Chittoor cluster (October 2026)
    # Typical rural logistics: Tata Ace / Bolero Pickup (1.5 - 2.5 ton capacity)
    BASE_RATES = {
        "Madanapalle APMC": {"distance_km": 115, "toll_inr": 80, "transit_hours": 2.5},
        "Tirupati Wholesale Hub": {"distance_km": 28, "toll_inr": 0, "transit_hours": 0.8},
        "Kolar APMC (Karnataka)": {"distance_km": 140, "toll_inr": 135, "transit_hours": 3.0},
        "Koyambedu Wholesale (Chennai)": {"distance_km": 135, "toll_inr": 160, "transit_hours": 3.2},
        "Bengaluru (Yeshwanthpur)": {"distance_km": 185, "toll_inr": 210, "transit_hours": 4.0},
        "Guntur Mirchi Yard": {"distance_km": 360, "toll_inr": 420, "transit_hours": 7.5}
    }

    # Fuel tariff: ~₹10.50/km shared vehicle cost + ₹1.50 per crate handling/loading
    @classmethod
    def calculate_freight(cls, destination_mandi: str, quantity_kg: float, modal_price_per_kg: float) -> Dict[str, Any]:
        info = cls.BASE_RATES.get(destination_mandi, cls.BASE_RATES["Tirupati Wholesale Hub"])
        dist = info["distance_km"]
        crates = math.ceil(quantity_kg / 25.0) # 25kg standard plastic crate

        # Shared pooled transit cost per kg decreases with load size
        vehicle_fuel_cost = dist * 11.0 # ₹11 per km for mini commercial freight
        pool_share_factor = min(1.0, max(0.25, quantity_kg / 1500.0)) # Shared backhaul factor
        allocated_fuel = vehicle_fuel_cost * pool_share_factor

        loading_unloading_cost = crates * 6.0 # ₹6 handling per crate at farmgate and mandi
        toll_share = info["toll_inr"] * pool_share_factor

        total_freight_inr = round(allocated_fuel + loading_unloading_cost + toll_share, 2)
        freight_per_kg = round(total_freight_inr / max(1.0, quantity_kg), 2)

        gross_revenue = round(quantity_kg * modal_price_per_kg, 2)
        net_profit_inr = round(gross_revenue - total_freight_inr, 2)
        net_rate_per_kg = round(net_profit_inr / max(1.0, quantity_kg), 2)

        return {
            "destination_mandi": destination_mandi,
            "origin": "Chennayyagunta / Chittoor Cluster",
            "distance_km": dist,
            "transit_hours": info["transit_hours"],
            "crate_count": crates,
            "gross_revenue": gross_revenue,
            "total_freight_cost": total_freight_inr,
            "freight_per_kg": freight_per_kg,
            "fuel_and_vehicle_cost": round(allocated_fuel, 2),
            "crate_handling_cost": round(loading_unloading_cost, 2),
            "toll_share": round(toll_share, 2),
            "net_take_home_profit": net_profit_inr,
            "net_realized_rate_per_kg": net_rate_per_kg,
            "is_profitable_vs_local": net_rate_per_kg > 30.0
        }

class WeighmentSlipService:
    @staticmethod
    def generate_slip_data(order_id: int, listing_id: int, farmer_name: str, phone: str, 
                             crop: str, grade: str, gross_kg: float, unit_price: float, 
                             advance_paid: float, final_balance: float, 
                             buyer_name: str, fpo_hub: str) -> Dict[str, Any]:
        tare_kg = round(gross_kg * 0.04, 2) # 4% standard crate/packaging weight
        net_kg = round(gross_kg - tare_kg, 2)
        total_payout = round(net_kg * unit_price, 2)

        return {
            "slip_number": f"AP-MANDI-WS-{order_id:05d}",
            "generated_at": datetime.now().strftime("%d-%b-%Y %I:%M %p"),
            "farmer": {
                "name": farmer_name,
                "phone": phone,
                "village": "Chennayyagunta",
                "district": "Chittoor, Andhra Pradesh",
                "fpo_hub": fpo_hub
            },
            "buyer": {
                "name": buyer_name,
                "terminal": "Tirupati Wholesale Hub",
                "license_no": "AP-APMC-TPT-8842"
            },
            "produce": {
                "commodity": crop,
                "quality_grade": grade,
                "gross_weight_kg": gross_kg,
                "tare_weight_kg": tare_kg,
                "net_payable_weight_kg": net_kg,
                "unit_rate_per_kg": unit_price
            },
            "financials": {
                "gross_amount": total_payout,
                "apmc_cess_exemption": "100% Waived (Direct Farmer-FPO Channel)",
                "advance_40_disbursed": advance_paid,
                "final_60_balance": final_balance,
                "payout_status": "COMPLETED & VERIFIED",
                "mode": "Instant Direct-UPI Escrow"
            }
        }
