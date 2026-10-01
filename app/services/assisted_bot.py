import re
from typing import Optional, Dict, Any

class AssistedBotService:
    @staticmethod
    def parse_farmer_message(sender: str, message: str) -> Optional[Dict[str, Any]]:
        text = message.strip()
        parts = [p.strip() for p in text.replace(";", ",").split(",")]

        if len(parts) >= 6:
            try:
                name = parts[0].replace("Farmer:", "").strip()
                hub = parts[1].replace("Hub:", "").strip()
                crop = parts[2].replace("Crop:", "").strip()
                
                qty_match = re.search(r"(\d+(\.\d+)?)", parts[3])
                qty = float(qty_match.group(1)) if qty_match else 100.0

                grade_raw = parts[4].upper()
                if "A" in grade_raw:
                    grade = "Grade A"
                elif "B" in grade_raw:
                    grade = "Grade B"
                else:
                    grade = "Grade C"

                mandi_match = re.search(r"(\d+(\.\d+)?)", parts[5])
                mandi_price = float(mandi_match.group(1)) if mandi_match else 20.0

                return {
                    "farmer_name": name,
                    "phone_number": sender,
                    "fpo_hub_id": hub,
                    "crop": crop.capitalize(),
                    "grade": grade,
                    "quantity_kg": qty,
                    "mandi_benchmark_price": mandi_price,
                    "is_perishable": True
                }
            except Exception:
                return None
        return None
