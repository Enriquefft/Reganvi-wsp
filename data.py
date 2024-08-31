"""Materials Valorization data."""

from typing import TypedDict


class MaterialData(TypedDict):
    """Material data structure."""

    item_id: int
    material: str
    price_kg: float
    price_ton: float


def transform_material_data(material_data: list[MaterialData]) -> str:
    """Transform the material data into a format understandable by GPT-4o."""
    transformed_data = "Materials data:\n"
    for material in material_data:
        transformed_data += (
            f"Item ID: {material['item_id']}, "
            f"Material name: {material['material']}, "
            f"Price per kg: {material['price_kg']} USD, "
            f"Price per ton: {material['price_ton']} USD.\n"
        )
    return transformed_data


material_data: list[MaterialData] = [
    {"item_id": 1, "material": "PAPEL BLANCO", "price_kg": 0.71, "price_ton": 710.00},
    {
        "item_id": 2,
        "material": "PERIODICO DE PRIMERA",
        "price_kg": 0.85,
        "price_ton": 850.00,
    },
    {
        "item_id": 3,
        "material": "COBRE BRILLANTE",
        "price_kg": 28.00,
        "price_ton": 28000.00,
    },
    {"item_id": 4, "material": "BRONCE", "price_kg": 14.00, "price_ton": 14000.00},
    {
        "item_id": 5,
        "material": "BATERIA CHICA",
        "price_kg": 15.00,
        "price_ton": 15000.00,
    },
    {
        "item_id": 6,
        "material": "BATERIA NORMAL",
        "price_kg": 19.00,
        "price_ton": 19000.00,
    },
    {
        "item_id": 7,
        "material": "BATERIA TORTUGA",
        "price_kg": 25.00,
        "price_ton": 25000.00,
    },
    {
        "item_id": 8,
        "material": "CHATARRA LIVIANA",
        "price_kg": 0.71,
        "price_ton": 710.00,
    },
    {
        "item_id": 9,
        "material": "CHATARRA PESADA",
        "price_kg": 0.73,
        "price_ton": 730.00,
    },
    {"item_id": 10, "material": "BOTELLAS PET", "price_kg": 2.90, "price_ton": 2900.00},
    {
        "item_id": 11,
        "material": "PLASTICO DURO",
        "price_kg": 1.50,
        "price_ton": 1500.00,
    },
    {
        "item_id": 12,
        "material": "PLASTICO FILL LIMPIO",
        "price_kg": 2.10,
        "price_ton": 2100.00,
    },
    {
        "item_id": 13,
        "material": "PLASTICO FILL SUCIO",
        "price_kg": 1.00,
        "price_ton": 1000.00,
    },
    {
        "item_id": 14,
        "material": "ALUMINIO LIVIANO",
        "price_kg": 4.50,
        "price_ton": 4500.00,
    },
    {
        "item_id": 15,
        "material": "ALUMINIO PESADO",
        "price_kg": 3.50,
        "price_ton": 3500.00,
    },
    {"item_id": 16, "material": "PVC", "price_kg": 1.20, "price_ton": 1200.00},
    {"item_id": 17, "material": "CARTON", "price_kg": 0.51, "price_ton": 510.00},
    {
        "item_id": 18,
        "material": "PAPEL MIXTO COLOR",
        "price_kg": 0.45,
        "price_ton": 450.00,
    },
    {"item_id": 19, "material": "VIDRIO", "price_kg": 0.28, "price_ton": 280.00},
    {"item_id": 20, "material": "TETRAPACK", "price_kg": 0.80, "price_ton": 800.00},
    {"item_id": 21, "material": "CARTOPLAS", "price_kg": 1.10, "price_ton": 1100.00},
    {"item_id": 22, "material": "MADERA LEÑA", "price_kg": 1.00, "price_ton": 1000.00},
    {
        "item_id": 23,
        "material": "LONA (ZAPATILLA)",
        "price_kg": 1.60,
        "price_ton": 1600.00,
    },
    {"item_id": 24, "material": "COCALATA", "price_kg": 1.40, "price_ton": 1400.00},
    {
        "item_id": 25,
        "material": "CAUCHOS (LLANTAS)",
        "price_kg": 0.10,
        "price_ton": 100.00,
    },
    {
        "item_id": 26,
        "material": "PAPEL DE REVISTA",
        "price_kg": 0.90,
        "price_ton": 900.00,
    },
    {"item_id": 27, "material": "ALTO IMPACTO", "price_kg": 3.50, "price_ton": 3500.00},
    {"item_id": 28, "material": "ACERO", "price_kg": 0.39, "price_ton": 390.00},
    {
        "item_id": 29,
        "material": "PET PRESADO COLORES",
        "price_kg": 1.50,
        "price_ton": 1500.00,
    },
    {
        "item_id": 30,
        "material": "PET PRESADO YOGURT",
        "price_kg": 1.61,
        "price_ton": 1610.00,
    },
    {
        "item_id": 31,
        "material": "PET PRESADO ACEITE",
        "price_kg": 0.60,
        "price_ton": 600.00,
    },
    {
        "item_id": 32,
        "material": "TAPITAS DE BOTELLA",
        "price_kg": 1.45,
        "price_ton": 1450.00,
    },
    {
        "item_id": 33,
        "material": "TAPITAS MOLIDA LIMPIA",
        "price_kg": 1.45,
        "price_ton": 1450.00,
    },
]

formatted_material_data= transform_material_data(material_data)
