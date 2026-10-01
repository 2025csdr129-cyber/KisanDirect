from app.schemas import PriceCorridorResponse

class PricingForecastingService:
    @staticmethod
    def calculate_price_corridor(crop: str, mandi_price: float, grade: str) -> PriceCorridorResponse:
        multipliers = {
            "Grade A": 1.15,
            "Grade B": 1.05,
            "Grade C": 0.90
        }
        grade_factor = multipliers.get(grade, 1.0)
        adjusted_mandi = mandi_price * grade_factor

        # Farmer guaranteed floor (+10% over mandi benchmark)
        farmer_floor = round(adjusted_mandi * 1.10, 2)
        
        # Traditional supply chains markup mandi prices by ~45%
        traditional_retail = adjusted_mandi * 1.45
        
        # Direct buyer price (-15% discount vs traditional retail)
        consumer_price = round(traditional_retail * 0.85, 2)
        
        savings = round(consumer_price - farmer_floor, 2)

        return PriceCorridorResponse(
            crop=crop,
            mandi_benchmark=mandi_price,
            recommended_farmer_price=farmer_floor,
            recommended_consumer_price=consumer_price,
            intermediary_savings_retained=savings
        )